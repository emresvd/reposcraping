import reposcraping

scraping = reposcraping.RepoScraping("https://github.com/emresvd/random-video")

scraping.clone_files("files")
