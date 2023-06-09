# Copyright (c) 2023 Nusab19 

import os
from setuptools import setup, find_packages

# Version
from nekobin import __version__ as v


# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


if os.path.isfile("README.md"):
    with open(("README.md"), encoding="utf-8") as readme:
        big_description = readme.read()

else:
    big_description = "pyNekobin - Paste Text into Nekobin with Python"





setup(name="pyNekobin",
      version=v,
      description="Paste codes to Nekobin.com with python",
      url="https://github.com/Nusab19/pyNekobin",
      author="Nusab Taha",
      author_email="nusabtaha33@gmail.com",
      license="MIT",
      packages=find_packages(),
      download_url=f"https://github.com/Nusab19/pyNekobin/releases/tag/pyNekobin-{v}",
      keywords=["Nekobin", "pyNekobin", "Paste Code", "Paste Bin"],
      long_description=big_description,
      long_description_content_type="text/markdown",
      
      package_data={"pyNekobin": ["data/*.json"]},
      include_package_data=True,
      
      install_requires=["httpx>=0.23.0"],
      python_requires = ">=3.6",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Topic :: Education",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
      ],
)
