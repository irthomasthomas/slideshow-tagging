from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="slideshow-tagging",
    description="A slideshow with zoom, star, and tagging support.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Thomasthomas Hughes",
    url="https://github.com/irthomasthomas/slideshow-tagging",
    project_urls={
        "Issues": "https://github.com/irthomasthomas/slideshow-tagging/issues",
        "CI": "https://github.com/irthomasthomas/slideshow-tagging/actions",
        "Changelog": "https://github.com/irthomasthomas/slideshow-tagging/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["slideshow_tagging"],
    entry_points="""
        [console_scripts]
        slideshow-tagging=slideshow_tagging.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.7",
)
