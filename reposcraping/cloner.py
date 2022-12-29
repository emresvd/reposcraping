import os
import urllib
import urllib.error

__package__ = "reposcraping"
RepoScraping = __import__("reposcraping").RepoScraping


class Cloner(object):
    def __init__(self, scraping) -> None:
        self.path: str = None
        self.filter_extension: str = None
        self.only_file_name: bool = False
        self.scraping: RepoScraping = scraping

    def clone(self) -> None:
        if not self.path:
            return

        if not os.path.isdir(self.path):
            os.mkdir(self.path)

        for url in self.scraping.file_urls:
            url = (
                url
                .replace("github.com", "raw.githubusercontent.com")
                .replace("blob/", "")
            )

            if self.only_file_name:
                file_name = url.split("/")[-1]
            else:
                file_name = "_".join(url.split("/")[3:]).replace("_master", "")

            full_path = os.path.join(self.path, file_name)

            if os.path.isfile(full_path):
                continue

            if self.filter_extension:
                if not file_name.endswith(self.filter_extension):
                    continue

            try:
                urllib.request.urlretrieve(url, full_path)
            except urllib.error.HTTPError:
                pass
