from setuptools import setup, find_packages
import codecs

with codecs.open("README.md", "r", "utf-8") as f:
    long_description = f.read()

setup(
    name='reposcraping',
    version='0.0.2',
    description='Scraping GitHub repository',
    long_description=long_description,
    author='emresvd',
    packages=find_packages(
        exclude=[
            'files',
        ],
    ),
    install_requires=[
        'beautifulsoup4==4.11.1',
        'requests==2.28.1',
    ],
    keywords=[
        'github',
        'scraping',
        'repository',
        'clone',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
)
