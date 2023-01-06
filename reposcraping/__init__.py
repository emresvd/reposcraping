from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import pickle
import os


class RepoScraping(object):
    def __init__(self, repo_url: str, p: bool = False, save: bool = False) -> None:
        self.repo_url = repo_url
        self.p = p
        self.save = save
        self.__start_prepare_file_urls = False

        self.__load_data()
        if not self.__start_prepare_file_urls:
            self.__prepare_tree_urls()
        self.__prepare_file_urls()
        self.__remove_cache()

    def __prepare_tree_urls(self) -> None:
        for i in self.tree_urls:
            r = requests.get(i)
            soup = BeautifulSoup(r.content, 'html.parser')

            for j in soup.find_all('a'):
                try:
                    if "tree/master" in j.get('href'):
                        url = urljoin(self.repo_url, j.get('href'))
                        if url not in self.tree_urls:
                            self.tree_urls.append(url)
                            if self.save:
                                with open('tree_urls.pkl', 'wb') as f:
                                    pickle.dump(self.tree_urls, f)
                            if self.p:
                                print(url)
                except TypeError:
                    pass

    def __prepare_file_urls(self) -> None:
        for tree_url in self.tree_urls:
            r = requests.get(tree_url)
            soup = BeautifulSoup(r.content, 'html.parser')

            for i in soup.find_all('a'):
                try:
                    if "blob/master" in i.get('href'):
                        url = urljoin(self.repo_url, i.get('href'))
                        if url not in self.file_urls:
                            self.file_urls.append(url)
                            if self.save:
                                with open('file_urls.pkl', 'wb') as f:
                                    pickle.dump(self.file_urls, f)
                            if self.p:
                                print(url)
                except TypeError:
                    pass

    def __load_data(self) -> None:
        if os.path.isfile('tree_urls.pkl'):
            with open('tree_urls.pkl', 'rb') as f:
                self.tree_urls = pickle.load(f)
            if self.p:
                print("\n".join(self.tree_urls))
        else:
            self.tree_urls = [self.repo_url]

        if os.path.isfile('file_urls.pkl'):
            self.__start_prepare_file_urls = True
            with open('file_urls.pkl', 'rb') as f:
                self.file_urls = pickle.load(f)
            if self.p:
                print("\n".join(self.file_urls))
        else:
            self.file_urls = []

    def __remove_cache(self) -> None:
        if self.save:
            for i in ["tree_urls.pkl", "file_urls.pkl"]:
                try:
                    os.remove(i)
                except FileNotFoundError:
                    continue
