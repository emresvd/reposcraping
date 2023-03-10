import sys

if sys.argv[-1] == "main.py":
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

if sys.argv[-1] == "clean":
    import shutil
    for i in ["build", "dist", "reposcraping.egg-info", "files"]:
        try:
            shutil.rmtree(i)
        except FileNotFoundError:
            pass

if sys.argv[-1] == "build":
    import os
    os.system("python setup.py sdist bdist_wheel")

if sys.argv[-1] == "upload":
    import os
    os.system("twine upload dist/*")
