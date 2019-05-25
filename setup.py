from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="game-of-life",
    version="0.0.1",
    description="Conway's Game of Life",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sudoandros/PythonDevelopment2019Project",
    packages=["game_of_life"],
    python_requires=">3, <4",
    entry_points={"console_scripts": ["game_of_life=game_of_life.gui:main"]},
)
