from reposcraping import RepoScraping
from reposcraping.cloner import Cloner

scraping = RepoScraping("https://github.com/emresvd/random-video")

print(scraping.tree_urls)
print(scraping.file_urls)

cloner = Cloner(scraping)
cloner.path = "files"
cloner.filter_extension = ".py"
cloner.only_file_name = True
cloner.clone(p=True)
