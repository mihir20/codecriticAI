from setuptools import setup, find_packages
import os
import re

def get_version():
    init = open(os.path.join("codecriticAI", "__init__.py")).read()
    return re.search(r"""__version__ = ["']{1,3}(.+?)["']{1,3}""", init).group(1)

setup(
    name="codecriticAI",
    version=get_version(),
    packages=find_packages(),
    install_requires=[
        "markdown",
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "codecriticAI=codecriticAI.main:main",
        ],
    },
    author="Mihir Gandhi",
    author_email="mihir20121997@gmail.com",
    description="An AI Code Review tool using OpenAI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mihir20/codecriticAI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)