"""
Download different Cloud images with one command.
"""

__author__ = "Officer K"
__version__ = 0.1

import subprocess

import click

import distro_dl
from distro_dl import fedora
from distro_dl import file
from distro_dl import ubuntu

subprocess.run("clear")


@click.command(no_args_is_help=True)
@click.argument("name", type=str)
@click.argument("version", type=str)
@click.option("--counter", default=1, type=int,
              help="You can set the number how many images you want to "
                   "download.")
def main(name, version, counter):
    if name == "fedora" and counter == 1:
        distro_dl.fedora.download(version)
    elif name == "fedora" and counter != 1:
        for number in range(1, counter + 1):
            distro_dl.fedora.download(version)
            distro_dl.file.rename(number, name)
    elif name == "ubuntu" and counter == 1:
        distro_dl.ubuntu.download(version)
    elif name == "ubuntu" and counter != 1:
        for number in range(1, counter + 1):
            distro_dl.ubuntu.download(version)
            distro_dl.file.rename(number, name)


if __name__ == "__main__":
    main()
