# datasette-execute-selected

<!-- [![PyPI](https://img.shields.io/pypi/v/datasette-execute-selected.svg)](https://pypi.org/project/datasette-execute-selected/)
[![Changelog](https://img.shields.io/github/v/release/simonw/datasette-execute-selected?include_prereleases&label=changelog)](https://github.com/simonw/datasette-execute-selected/releases) -->
[![Tests](https://github.com/simonw/datasette-execute-selected/workflows/Test/badge.svg)](https://github.com/simonw/datasette-execute-selected/actions?execute=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-execute-selected/blob/main/LICENSE)

Execute selected fragments of a query

> **This is a work in progress**. It doesn't actually work yet.

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-execute-selected

## Usage

Once this plugin is working, you'll be able to select a fragment of SQL inside a larger editable query and, if that fragment can be executed, an "Execute selected SQL" button will be shown.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-execute-selected
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
