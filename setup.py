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
    name="datasette-execute-selected",
    description="Execute selected fragments of a query",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-execute-selected",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-execute-selected/issues",
        "CI": "https://github.com/simonw/datasette-execute-selected/actions",
        "Changelog": "https://github.com/simonw/datasette-execute-selected/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_execute_selected"],
    entry_points={"datasette": ["execute_selected = datasette_execute_selected"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    package_data={"datasette_execute_selected": ["static/*"]},
    python_requires=">=3.7",
)
