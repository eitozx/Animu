import setuptools 
import animu

version = animu.__version__
author = animu.__author__

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name = "animu",
    author = author,
    author_email = "iameitozx@gmail.com",
    url = "http://github.com/EitoZX/Animu",
    version = version,
    description = "An async wrapper for Animu API written in Python.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(),
    license_files = "LICENSE",
    install_requires = requirements,
    keywords = ['animu-api','anime','anime-quotes', 'anime-api', 'animeapi', 'animu', 'anime-quotes-api',],
)