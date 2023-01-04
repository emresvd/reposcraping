from setuptools import setup, find_packages
import codecs

with codecs.open("README.md", "r", "utf-8") as f:
    long_description = f.read()

setup(
    name='reposcraping',
    version='1.0.3',
    description='Scraping GitHub repository',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='emresvd',
    license='MIT',
    url='https://github.com/emresvd/reposcraping',
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
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
