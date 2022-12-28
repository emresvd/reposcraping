from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urljoin
import urllib.request
import urllib.error
import os


class RepoScraping(object):
    def __init__(self, repo_url: str) -> None:
        self.repo_url = repo_url
        r = requests.get(self.repo_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        self.tree_urls = [self.repo_url]
        self.file_urls = []
        self.__prepare_tree_urls()
        self.__prepare_file_urls()

    def __prepare_tree_urls(self):
        for i in self.tree_urls:
            r = requests.get(i)
            soup = BeautifulSoup(r.content, 'html.parser')
            for j in soup.find_all('a'):
                if "tree/master" in j.get('href'):
                    url = urljoin(self.repo_url, j.get('href'))
                    if url not in self.tree_urls:
                        self.tree_urls.append(url)

    def __prepare_file_urls(self):
        for tree_url in self.tree_urls:
            r = requests.get(tree_url)
            soup = BeautifulSoup(r.content, 'html.parser')

            for i in soup.find_all('a'):
                if "blob/master" in i.get('href'):
                    url = urljoin(self.repo_url, i.get('href'))
                    if url not in self.file_urls:
                        self.file_urls.append(url)

    def clone_files(self, path: str, fiter: str = None):
        if not os.path.isdir(path):
            os.mkdir(path)

        for url in self.urls:
            url = (
                url
                .replace("github.com", "raw.githubusercontent.com")
                .replace("blob/", "")
            )

            file_name = url.split("/")[-1]
            path = os.path.join(path, file_name)

            if filter:
                if not file_name.endswith(filter):
                    continue

            try:
                urllib.request.urlretrieve(url, path)
            except urllib.error.HTTPError:
                pass

            if os.path.isfile(os.path.join(path, file_name)):
                return False

        return True