import reposcraping

scraping = reposcraping.RepoScraping("https://github.com/emresvd/random-video")

f = scraping.file_urls
print(len(f))