from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nepali_date_utils",
    version="0.3",
    description="Convert Nepali to English Dates: Easily switch between Nepali and English dates with this Python package.",
    author="Niraj Adhikari",
    author_email="nrjadkry@gmail.com",
    packages=find_packages(),
    license="GPLv3",
    url="https://github.com/nrjadkry/nepali-date-utils",
    install_requires=[],
    keywords=["date", "nepali-date"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: GIS",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3.8",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
