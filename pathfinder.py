"""
Download different Cloud images with one command.
"""

__author__ = "Officer K"
__version__ = 0.1

import subprocess

import click

import distro_dl
from distro_dl import fedora_dl
from distro_dl import ubuntu_dl

subprocess.run("clear")


@click.command()
@click.argument("name", type=str)
@click.argument("version", type=str)
def main(name, version):
    if name == "fedora":
        distro_dl.fedora_dl.download(version)
    elif name == "ubuntu":
        distro_dl.ubuntu_dl.download(version)


if __name__ == "__main__":
    main()
