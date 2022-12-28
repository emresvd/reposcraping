import reposcraping

scraping = reposcraping.RepoScraping("https://github.com/emresvd/random-video")

print(scraping.file_urls)