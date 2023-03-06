from reposcraping import RepoScraping
from reposcraping.cloner import Cloner
import os
import shutil

if os.path.isdir("files"):
    shutil.rmtree("files")

scraping = RepoScraping("https://github.com/emresvd/random-video")

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
print("✓ file_urls test passed\n")


cloner = Cloner(scraping)
cloner.clone(
    paths={
        ".py": "files/python_files",
        ".txt": "files/text_files",
        ".md": "files/markdown_files",
        ".html": "files/html_files",
        "": "files/other_files",
    },
)

print("\nlooking for files")
assert set(os.listdir("files")) == set([
    'html_files',
    'markdown_files',
    'other_files',
    'python_files',
    'text_files'
])
print("✓ files found")

print("\nlooking for html files")
assert set(os.listdir("files/html_files")) == set([
    'emresvd_random-video_templates_download.html',
    'emresvd_random-video_templates_index.html'
])
print("✓ html files found")

print("\nlooking for markdown files")
assert set(os.listdir("files/markdown_files")) == set([
    'emresvd_random-video_LICENSE.md',
    'emresvd_random-video_README.md'
])
print("✓ markdown files found")

print("\nlooking for other files")
assert set(os.listdir("files/other_files")) == set([
    'emresvd_random-video_.gitignore',
    'emresvd_random-video_db.sqlite3',
    'emresvd_random-video_random_video___pycache___settings.cpython-37.pyc',
    'emresvd_random-video_random_video___pycache___urls.cpython-37.pyc',
    'emresvd_random-video_random_video___pycache___wsgi.cpython-37.pyc',
    'emresvd_random-video_random_video___pycache_____init__.cpython-37.pyc',
    'emresvd_random-video_static_favicon.ico',
    'emresvd_random-video_static_ic_launcher-playstore.png',
    'emresvd_random-video_video_migrations___pycache_____init__.cpython-37.pyc',
    'emresvd_random-video_video___pycache___admin.cpython-37.pyc',
    'emresvd_random-video_video___pycache___models.cpython-37.pyc',
    'emresvd_random-video_video___pycache___random_video.cpython-37.pyc',
    'emresvd_random-video_video___pycache___views.cpython-37.pyc',
    'emresvd_random-video_video___pycache_____init__.cpython-37.pyc'
])
print("✓ other files found")

print("\nlooking for python files")
assert set(os.listdir("files/python_files")) == set([
    'emresvd_random-video_manage.py',
    'emresvd_random-video_random_video_asgi.py',
    'emresvd_random-video_random_video_settings.py',
    'emresvd_random-video_random_video_urls.py',
    'emresvd_random-video_random_video_wsgi.py',
    'emresvd_random-video_random_video___init__.py',
    'emresvd_random-video_video_admin.py',
    'emresvd_random-video_video_apps.py',
    'emresvd_random-video_video_migrations___init__.py',
    'emresvd_random-video_video_models.py',
    'emresvd_random-video_video_random_video.py',
    'emresvd_random-video_video_tests.py',
    'emresvd_random-video_video_views.py',
    'emresvd_random-video_video___init__.py'
])
print("✓ python files found")

print("\nlooking for text files")
assert set(os.listdir("files/text_files")) == set([
    'emresvd_random-video_requirements.txt',
    'emresvd_random-video_special_search_car.txt',
    'emresvd_random-video_special_search_food.txt',
    'emresvd_random-video_special_search_rocket.txt',
    'emresvd_random-video_special_search_space.txt',
    'emresvd_random-video_special_search_travel.txt',
    'emresvd_random-video_words.txt'
])
print("✓ text files found")

print("\n✓ all tests passed")
