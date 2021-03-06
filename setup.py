import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="python-simple-cli",
    version="0.0.1",
    description="Simple CLI",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/enigma0Z/python-simple-cli.git",
    author="Johnathan Bell",
    author_email="enigma.0Z@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ],
    packages=["SimpleCli"],
    include_package_data=True,
    install_requires=[""],
    entry_points={}
)
