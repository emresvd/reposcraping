from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urljoin

repo_url = sys.argv[-1]

r = requests.get(repo_url)
soup = BeautifulSoup(r.content, 'html.parser')

# for i in soup.find_all('a'):
#     if "blob/master" in i.get('href'):
#         url = (
#             urljoin(repo_url, i.get('href'))
#             .replace("github.com", "raw.githubusercontent.com")
#             .replace("blob/", "")
#         )
#         print(url)

folder_urls = [repo_url]

for i in folder_urls:
    print("-", end="")
    r = requests.get(i)
    soup = BeautifulSoup(r.content, 'html.parser')
    for j in soup.find_all('a'):
        if "tree/master" in j.get('href'):
            url = urljoin(repo_url, j.get('href'))
            if url not in folder_urls:
                folder_urls.append(url)

print(folder_urls)
