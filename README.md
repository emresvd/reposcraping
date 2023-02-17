# [reposcraping](https://pypi.org/project/reposcraping/)
### Scraping GitHub repository
This library allows you to access the names of files and folders of any GitHub repository. Cloner class allows you to clone the file types you want to the path you want.<br>
## downloads
[![Downloads](https://static.pepy.tech/badge/reposcraping)](https://pepy.tech/project/reposcraping) [![Downloads](https://static.pepy.tech/badge/reposcraping/month)](https://pepy.tech/project/reposcraping) [![Downloads](https://static.pepy.tech/badge/reposcraping/week)](https://pepy.tech/project/reposcraping)
## setup
```bash
pip install reposcraping
```
## usage
```python
from reposcraping import RepoScraping
from reposcraping.cloner import Cloner

scraping = RepoScraping(
    "https://github.com/emresvd/random-video",
    p=True,
)

print(scraping.tree_urls)
print(scraping.file_urls)

cloner = Cloner(scraping)
cloner.clone(
    paths={
        ".py": "files/python_files",
        ".txt": "files/text_files",
        ".md": "files/markdown_files",
        ".html": "files/html_files",
        "": "files/other_files",
    },
    only_file_name=True,
    p=True,
)
```
