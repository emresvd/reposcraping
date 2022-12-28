from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urljoin
import urllib.request
import urllib.error
import os


class RepoScraping(object):
    def __init__(self, repo_url) -> None:
        self.repo_url = repo_url
        r = requests.get(self.repo_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        self.tree_urls = [self.repo_url]

    def get_tree_urls(self):
        for i in self.tree_urls:
            r = requests.get(i)
            soup = BeautifulSoup(r.content, 'html.parser')
            for j in soup.find_all('a'):
                if "tree/master" in j.get('href'):
                    url = urljoin(self.repo_url, j.get('href'))
                    if url not in self.tree_urls:
                        self.tree_urls.append(url)
