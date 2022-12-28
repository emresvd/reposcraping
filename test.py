import reposcraping

scraping = reposcraping.RepoScraping("https://github.com/emresvd/random-video")

print(len(scraping.file_urls))
scraping.clone_files("files")
