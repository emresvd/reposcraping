```python
import reposcraping

scraping = reposcraping.RepoScraping("https://github.com/emresvd/random-video")

scraping.clone_files("files", filter_extension=".py", only_file_name=True)

```