"""
Download different Cloud images with one command.
"""

__author__ = "Officer K"
__version__ = 0.1

import subprocess

import click

import distro_dl
from distro_dl import download
from distro_dl import file

subprocess.run("clear")


@click.command(no_args_is_help=True)
@click.argument("name", type=str)
@click.argument("version", type=str)
@click.option("--count", default=1, type=int, show_default=True,
              help="You can set the number how many images you want to download.")
def main(name, version, count):
    if count != 1:
        for number in range(1, count+1):
            distro_dl.download.image(name, version)
            distro_dl.file.rename(name, number)
    else:
        distro_dl.download.image(name, version)


if __name__ == "__main__":
    main()
