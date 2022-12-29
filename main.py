import reposcraping
from reposcraping import cloner

scraping = reposcraping.RepoScraping("https://github.com/emresvd/random-video")

print(scraping.tree_urls)
print(scraping.file_urls)

clone = cloner.Cloner(scraping)
clone.path = "files"
clone.filter_extension = ".py"
clone.only_file_name = True
clone.clone()
