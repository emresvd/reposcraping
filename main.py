import sys

if sys.argv[-1] == "main.py":
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

if sys.argv[-1] == "clean":
    import shutil
    for i in ["build", "dist", "reposcraping.egg-info"]:
        shutil.rmtree(i)

if sys.argv[-1] == "build":
    import os
    os.system("python setup.py sdist bdist_wheel")

if sys.argv[-1] == "upload":
    import os
    os.system("twine upload dist/*")
