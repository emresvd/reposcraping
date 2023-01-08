import os
import urllib
import urllib.error

__package__ = "reposcraping"
RepoScraping = __import__("reposcraping").RepoScraping


class Cloner(object):
    def __init__(self, scraping: RepoScraping) -> None:
        self.scraping: RepoScraping = scraping

    def clone(
        self,
        paths: dict,
        only_file_name: False,
        p: bool = False
    ) -> None:

        for i in paths:
            path = paths[i]
            if not os.path.isdir(path):
                os.makedirs(path, exist_ok=True)

        for url in self.scraping.file_urls:
            url = (
                url
                .replace("github.com", "raw.githubusercontent.com")
                .replace("blob/", "")
            )

            if only_file_name:
                file_name = url.split("/")[-1]
            else:
                file_name = "_".join(url.split("/")[3:]).replace("_master", "")

            path = self.__get_path_by_extension(paths, file_name)
            if not path:
                continue

            full_path = os.path.join(path, file_name)

            if os.path.isfile(full_path):
                continue

            try:
                if p:
                    print(full_path)
                urllib.request.urlretrieve(url, full_path)
            except urllib.error.HTTPError:
                pass

    def __get_path_by_extension(self, paths: dict, file_name: str) -> str:
        if paths:
            for i in paths:
                if file_name.endswith(i):
                    return paths[i]
        return None
