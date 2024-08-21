from setuptools import setup, find_packages

setup(
    name="dvlib",
    version="0.0.1",
    author="Cherupally Naveenchandra",
    author_email="cherupallynaveen@gmail.com",
    url="https://github.com/ChandraCherupally/",
    description="Data validation main functions",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    entry_points={"console_scripts": ["dvlib = src.main_functs:main"]},
)
