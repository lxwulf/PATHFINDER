"""
Setup to download fedora cloud images.
"""

import requests
from bs4 import BeautifulSoup as BS4_Crawler
from tqdm import tqdm

STATUS = 200
FILETYPE = "qcow2"


def get_link(source):
    return BS4_Crawler(requests.get(source).text, 'html.parser')


def download(version):

    MAIN_SOURCE = f"http://ftp.usf.edu/pub/fedora/linux/releases/{version}/" \
                  f"Cloud/x86_64/images/"

    for LINKS in get_link(MAIN_SOURCE).findAll('a'):
        IMAGE_LINK = LINKS.get('href')

        GET_FILE = requests.get(MAIN_SOURCE + IMAGE_LINK, stream=True)

        if STATUS == GET_FILE.status_code and FILETYPE in IMAGE_LINK:

            with open(LINKS.text, 'wb') as TARGET_FILE, tqdm(
                    desc=IMAGE_LINK,
                    total=int(GET_FILE.headers.get("Content-Length", "0")),
                    colour="green",
                    unit="iB",
                    unit_scale=True,
                    unit_divisor=1024
            ) as progressbar:

                for DATA in GET_FILE.iter_content(chunk_size=1024):
                    SIZE = TARGET_FILE.write(DATA)
                    progressbar.update(SIZE)
                progressbar.close()
                TARGET_FILE.close()
