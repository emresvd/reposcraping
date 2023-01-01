from bs4 import BeautifulSoup as _BeautifulSoup
import requests as _requests
from urllib.parse import urljoin as _urljoin


class RepoScraping(object):
    def __init__(self, repo_url: str) -> None:
        self.repo_url = repo_url

        self.tree_urls = [self.repo_url]
        self.file_urls = []

        self.__prepare_tree_urls()
        self.__prepare_file_urls()

    def __prepare_tree_urls(self) -> None:
        for i in self.tree_urls:
            r = _requests.get(i)
            soup = _BeautifulSoup(r.content, 'html.parser')

            for j in soup.find_all('a'):
                if "tree/master" in j.get('href'):
                    url = _urljoin(self.repo_url, j.get('href'))
                    if url not in self.tree_urls:
                        self.tree_urls.append(url)

    def __prepare_file_urls(self) -> None:
        for tree_url in self.tree_urls:
            r = _requests.get(tree_url)
            soup = _BeautifulSoup(r.content, 'html.parser')

            for i in soup.find_all('a'):
                if "blob/master" in i.get('href'):
                    url = _urljoin(self.repo_url, i.get('href'))
                    if url not in self.file_urls:
                        self.file_urls.append(url)
