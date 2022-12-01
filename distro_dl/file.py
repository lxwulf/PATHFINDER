import pathlib
from pathlib import Path


def rename(number, name):
    path = Path(".")
    if name == "fedora":
        directory = list(path.glob("*.x86_64.qcow2"))
        for disk in directory:
            disk.rename(pathlib.Path(disk.parent,
                        f"{disk.stem}-{number:02d}{disk.suffix}"))
    elif name == "ubuntu":
        directory = list(path.glob("*disk-kvm.img"))
        for disk in directory:
            disk.rename(pathlib.Path(disk.parent,
                        f"{disk.stem}-{number:02d}{disk.suffix}"))
