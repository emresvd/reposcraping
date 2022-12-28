from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urljoin
import urllib.request
import urllib.error
import os

repo_url = sys.argv[-1]

r = requests.get(repo_url)
soup = BeautifulSoup(r.content, 'html.parser')

tree_urls = [repo_url]

# get tree urls
for i in tree_urls:
    r = requests.get(i)
    soup = BeautifulSoup(r.content, 'html.parser')
    for j in soup.find_all('a'):
        if "tree/master" in j.get('href'):
            url = urljoin(repo_url, j.get('href'))
            if url not in tree_urls:
                tree_urls.append(url)

urls = []

# get file urls
for tree_url in tree_urls:
    r = requests.get(tree_url)
    soup = BeautifulSoup(r.content, 'html.parser')

    for i in soup.find_all('a'):
        if "blob/master" in i.get('href'):
            url = urljoin(repo_url, i.get('href'))
            if url not in urls:
                urls.append(url)

with open("urls.txt", "w") as f:
    f.write("\n".join(urls))

if not os.path.isdir("files"):
    os.mkdir("files")

# clone files
for url in urls:
    url = (
        url
        .replace("github.com", "raw.githubusercontent.com")
        .replace("blob/", "")
    )

    file_name = url.split("/")[-1]
    path = "files/"+file_name

    try:
        urllib.request.urlretrieve(url, path)
    except urllib.error.HTTPError:
        pass
