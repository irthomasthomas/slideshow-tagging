# slideshow-tagging

[![PyPI](https://img.shields.io/pypi/v/slideshow-tagging.svg)](https://pypi.org/project/slideshow-tagging/)
[![Changelog](https://img.shields.io/github/v/release/irthomasthomas/slideshow-tagging?include_prereleases&label=changelog)](https://github.com/irthomasthomas/slideshow-tagging/releases)
[![Tests](https://github.com/irthomasthomas/slideshow-tagging/workflows/Test/badge.svg)](https://github.com/irthomasthomas/slideshow-tagging/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/irthomasthomas/slideshow-tagging/blob/master/LICENSE)

A slideshow with zoom, star, and tagging support.

## Installation

Install this tool using `pip`:

    pip install slideshow-tagging

## Usage

For help, run:

    slideshow-tagging --help

You can also use:

    python -m slideshow_tagging --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd slideshow-tagging
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
