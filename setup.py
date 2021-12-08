from setuptools import setup

setup(
    name = "soli",
    version = "1.0.0",
    description = "ls clone",
    author = "JeffTheK",
    url = "https://github.com/JeffTheK/soli",
    packages = ["soli"],
    entry_points = {
        'console_scripts': [
            'soli = soli.__main__:main'
        ]
    },
)