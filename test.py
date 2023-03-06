from reposcraping import RepoScraping
from reposcraping.cloner import Cloner

scraping = RepoScraping(
    "https://github.com/emresvd/random-video",
    p=True
)

print("\ntesting tree_urls")
assert scraping.tree_urls == [
    'https://github.com/emresvd/random-video',
    'https://github.com/emresvd/random-video/tree/master/random_video',
    'https://github.com/emresvd/random-video/tree/master/special_search',
    'https://github.com/emresvd/random-video/tree/master/static',
    'https://github.com/emresvd/random-video/tree/master/templates',
    'https://github.com/emresvd/random-video/tree/master/video',
    'https://github.com/emresvd/random-video/tree/master/random_video/__pycache__',
    'https://github.com/emresvd/random-video/tree/master/video/__pycache__',
    'https://github.com/emresvd/random-video/tree/master/video/migrations',
    'https://github.com/emresvd/random-video/tree/master/video/migrations/__pycache__'
]
print("✓ tree_urls test passed")

print("\ntesting file_urls")
assert scraping.file_urls == [
    'https://github.com/emresvd/random-video/blob/master/LICENSE.md',
    'https://github.com/emresvd/random-video/blob/master/.gitignore',
    'https://github.com/emresvd/random-video/blob/master/README.md',
    'https://github.com/emresvd/random-video/blob/master/db.sqlite3',
    'https://github.com/emresvd/random-video/blob/master/manage.py',
    'https://github.com/emresvd/random-video/blob/master/requirements.txt',
    'https://github.com/emresvd/random-video/blob/master/words.txt',
    'https://github.com/emresvd/random-video/blob/master/static/ic_launcher-playstore.png',
    'https://github.com/emresvd/random-video/blob/master/random_video/__init__.py',
    'https://github.com/emresvd/random-video/blob/master/random_video/asgi.py',
    'https://github.com/emresvd/random-video/blob/master/random_video/settings.py',
    'https://github.com/emresvd/random-video/blob/master/random_video/urls.py',
    'https://github.com/emresvd/random-video/blob/master/random_video/wsgi.py',
    'https://github.com/emresvd/random-video/blob/master/special_search/car.txt',
    'https://github.com/emresvd/random-video/blob/master/special_search/food.txt',
    'https://github.com/emresvd/random-video/blob/master/special_search/rocket.txt',
    'https://github.com/emresvd/random-video/blob/master/special_search/space.txt',
    'https://github.com/emresvd/random-video/blob/master/special_search/travel.txt',
    'https://github.com/emresvd/random-video/blob/master/static/favicon.ico',
    'https://github.com/emresvd/random-video/blob/master/templates/download.html',
    'https://github.com/emresvd/random-video/blob/master/templates/index.html',
    'https://github.com/emresvd/random-video/blob/master/video/__init__.py',
    'https://github.com/emresvd/random-video/blob/master/video/admin.py',
    'https://github.com/emresvd/random-video/blob/master/video/apps.py',
    'https://github.com/emresvd/random-video/blob/master/video/models.py',
    'https://github.com/emresvd/random-video/blob/master/video/random_video.py',
    'https://github.com/emresvd/random-video/blob/master/video/tests.py',
    'https://github.com/emresvd/random-video/blob/master/video/views.py',
    'https://github.com/emresvd/random-video/blob/master/random_video/__pycache__/__init__.cpython-37.pyc',
    'https://github.com/emresvd/random-video/blob/master/random_video/__pycache__/settings.cpython-37.pyc',
    'https://github.com/emresvd/random-video/blob/master/random_video/__pycache__/urls.cpython-37.pyc',
    'https://github.com/emresvd/random-video/blob/master/random_video/__pycache__/wsgi.cpython-37.pyc',
    'https://github.com/emresvd/random-video/blob/master/video/__pycache__/__init__.cpython-37.pyc',
    'https://github.com/emresvd/random-video/blob/master/video/__pycache__/admin.cpython-37.pyc',
    'https://github.com/emresvd/random-video/blob/master/video/__pycache__/models.cpython-37.pyc',
    'https://github.com/emresvd/random-video/blob/master/video/__pycache__/random_video.cpython-37.pyc',
    'https://github.com/emresvd/random-video/blob/master/video/__pycache__/views.cpython-37.pyc',
    'https://github.com/emresvd/random-video/blob/master/video/migrations/__init__.py',
    'https://github.com/emresvd/random-video/blob/master/video/migrations/__pycache__/__init__.cpython-37.pyc'
]
print("✓ file_urls test passed")
