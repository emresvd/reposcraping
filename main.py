from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urljoin

repo_url = sys.argv[-1]

r = requests.get(repo_url)
soup = BeautifulSoup(r.content, 'html.parser')

# print(soup.prettify())

for i in soup.find_all('a'):
    if "blob/master" in i.get('href'):
        url = (
            urljoin(repo_url, i.get('href'))
            .replace("github.com", "raw.githubusercontent.com")
            .replace("blob/", "")
        )
        print(url)
