from reposcraping import RepoScraping
from reposcraping.cloner import Cloner
import unittest
import shutil
import os

if os.path.isdir("files"):
    shutil.rmtree("files")

scraping = RepoScraping("https://github.com/emresvd/random-video", p=True)

cloner = Cloner(scraping)
cloner.clone(
    paths={
        ".py": "files/python_files",
        ".txt": "files/text_files",
        ".md": "files/markdown_files",
        ".html": "files/html_files",
        "": "files/other_files",
    },
    p=True
)


class Test(unittest.TestCase):
    maxDiff = None

    def test_tree_urls(self):
        self.assertEqual(
            set(scraping.tree_urls),
            set([
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
            ])
        )

    def test_file_urls(self):
        self.assertEqual(
            set(scraping.file_urls),
            set([
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
            ])
        )

    def test_files(self):
        self.assertEqual(
            set(os.listdir("files")),
            set([
                'python_files',
                'text_files',
                'markdown_files',
                'html_files',
                'other_files',
            ])
        )

    def test_python_files(self):
        self.assertEqual(
            set(os.listdir("files/python_files")),
            set([
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
        )

    def test_text_files(self):
        self.assertEqual(
            set(os.listdir("files/text_files")),
            set([
                'emresvd_random-video_requirements.txt',
                'emresvd_random-video_special_search_car.txt',
                'emresvd_random-video_special_search_food.txt',
                'emresvd_random-video_special_search_rocket.txt',
                'emresvd_random-video_special_search_space.txt',
                'emresvd_random-video_special_search_travel.txt',
                'emresvd_random-video_words.txt'
            ])
        )

    def test_markdown_files(self):
        self.assertEqual(
            set(os.listdir("files/markdown_files")),
            set([
                'emresvd_random-video_LICENSE.md',
                'emresvd_random-video_README.md'
            ])
        )

    def test_html_files(self):
        self.assertEqual(
            set(os.listdir("files/html_files")),
            set([
                'emresvd_random-video_templates_download.html',
                'emresvd_random-video_templates_index.html'
            ])
        )

    def test_other_files(self):
        self.assertEqual(
            set(os.listdir("files/other_files")),
            set([
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
        )


if __name__ == "__main__":
    unittest.main()
