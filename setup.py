from pathlib import Path
from setuptools import setup
from os import path

here = Path(__file__).parent.resolve()

with open(here / "README.md") as file:
    long_description = file.read()

data_files = [str(here / "game_of_life" / "patterns.json")]
for path in (here / "game_of_life" / "locale").glob('**/*.mo'):
    data_files.append(str(path))
for path in (here / "game_of_life" / "locale").glob('**/*.po'):
    data_files.append(str(path))

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
    package_data={"game_of_life": data_files},
)
