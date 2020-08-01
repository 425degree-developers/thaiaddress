#! /usr/bin/env python
import os.path as op
from setuptools import setup, find_packages


def get_version():
    """
    Get the version without importing, so as not to invoke dependency
    requirements.
    """
    base, _ = op.split(op.realpath(__file__))
    file = op.join(base, "thaiaddress", "__init__.py")

    for line in open(file, "r"):
        if "__version__" in line:
            return line.split("=")[1].strip().strip("'").strip('"')


if __name__ == "__main__":
    setup(
        name="thaiaddress",
        version=get_version(),
        description="A Python parser for Thai address",
        long_description=open("README.md").read(),
        long_description_content_type='text/markdown',
        python_requires=">=3.6",
        url="https://github.com/425degree-developers/thaiaddress",
        download_url="https://github.com/425degree-developers/thaiaddress.git",
        author="Titipat Achakulvisut",
        author_email="my.titipat@gmail.com",
        license="Apache Software License 2.0 (c) 2020 Titipat Achakulvisut, 425 Degree Co., Bangkok, Thailand",
        install_requires=[
            "joblib",
            "deepcut",
            "spacy",
            "pythainlp",
            "sklearn_crfsuite",
            "numpy",
            "pytest",
            "pytest-cov",
            "scikit-learn",
            "jsonlines",
            "fuzzywuzzy",
            "pandas"
        ],
        packages=find_packages(),
        include_package_data=True,
        keywords=[
            "Parser",
            "Address",
            "Thai Address",
            "Thai Natural Language Processing",
            "Natural Language Processing",
        ],
        classifiers=[
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Unix",
            "Operating System :: MacOS",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        platforms="any",
        project_urls={
            "Source": "https://github.com/425degree-developers/thaiaddress",
            "Documentation": "https://github.com/425degree-developers/thaiaddress",
            "Bug Reports": "https://github.com/425degree-developers/thaiaddress/issues",
        },
    )
