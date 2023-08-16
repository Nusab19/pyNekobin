# Copyright (c) 2023 Nusab19

import os
from setuptools import setup

# Version
version = "3.1"

# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


if os.path.isfile("README.md"):
    with open(("README.md"), encoding="utf-8") as readme:
        big_description = readme.read()

else:
    big_description = "PyNekobin - Paste Text into Nekobin.com with Python"


setup(name="pyNekobin",
      version=version,
      description="Paste codes to Nekobin.com with python",
      url="https://github.com/Nusab19/pyNekobin",
      author="Nusab Taha",
      author_email="nusabtaha33@gmail.com",
      license="MIT",
      download_url=f"https://github.com/Nusab19/pyNekobin/releases/tag/pyNekobin-{version}",
      keywords=["Nekobin", "pyNekobin", "Paste Code", "Paste Bin"],
      long_description=big_description,
      long_description_content_type="text/markdown",

      package_data={"pyNekobin": ["data/*.json"]},
      include_package_data=True,

      packages=["nekobin"],
      install_requires=["httpx"],
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
      ]
      )
