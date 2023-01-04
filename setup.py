from setuptools import setup, find_packages

setup(
    name='reposcraping',
    version='0.0.1',
    description='Scraping GitHub repository',
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
