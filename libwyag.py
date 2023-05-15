"""Module with cli tool for git[diy]
   the code/flow is written based on this https://wyag.thb.lt/
   but using typer to create a proper cli interface and ease the writing
"""
import typer
from collections import OrderedDict
from git_repository import create_repo
import configparser  # git uses microsofts;s ini format and to read and write files in that we use this lib
import hashlib
from math import ceil
import os
import sys
import zlib
import re


app = typer.Typer()


# defining a command using decorator
@app.command()
def add() -> None:
    pass


@app.command()
def cat_file():
    pass


@app.command()
def checkout():
    pass


@app.command()
def commit():
    pass


@app.command()
def hash_object():
    pass


@app.command()
def init(path: str):
    """Command to initialise the repository
    """
    create_repo(path)


@app.command()
def log():
    pass


@app.command()
def ls_files():
    pass


@app.command()
def ls_tree():
    pass


@app.command()
def merge():
    pass


@app.command()
def rebase():
    pass


@app.command()
def rev_parse():
    pass


@app.command()
def rm():
    pass


@app.command()
def show_ref():
    pass


@app.command()
def tag():
    pass


def main():
    """Method to start the app instead of using argparse using typers
    command decorator to map the commands
    """
    app()


if __name__ == "__main__":
    main()
