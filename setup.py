import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="Silly_Anonymizer",
    version="1.0.0",
    description="Anonymize users",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Curious-Joe/Anonymizer.git",
    author="Arafath Hossain",
    author_email="a.h.fahad90@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True
)