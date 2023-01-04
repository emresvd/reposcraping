import sys
import os
import shutil

if sys.argv[-1] == "clean":
    for i in ["build", "dist", "reposcraping.egg-info"]:
        shutil.rmtree(i)

if sys.argv[-1] == "build":
    os.system("python setup.py sdist bdist_wheel")

if sys.argv[-1] == "upload":
    os.system("twine upload dist/*")
