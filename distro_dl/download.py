"""
Setup to download the images.
"""

import requests
from bs4 import BeautifulSoup as BS4_Crawler
from tqdm import tqdm

STATUS = 200
FILETYPE = "qcow2"


def get_link(source):
    return BS4_Crawler(requests.get(source).text, "html.parser")


def image(name, version):

    main_source = f"http://ftp.usf.edu/pub/fedora/linux/releases/{version}/" \
                  f"Cloud/x86_64/images/"

    for LINKS in get_link(main_source).findAll('a'):
        image_link = LINKS.get('href')

        get_file = requests.get(main_source + image_link, stream=True)

        if STATUS == get_file.status_code and FILETYPE in image_link:

            with open(LINKS.text, 'wb') as TARGET_FILE, tqdm(
                    desc=image_link,
                    total=int(get_file.headers.get("Content-Length", "0")),
                    colour="green",
                    unit="iB",
                    unit_scale=True,
                    unit_divisor=1024
            ) as progressbar:

                for DATA in get_file.iter_content(chunk_size=1024):
                    size = TARGET_FILE.write(DATA)
                    progressbar.update(size)
                progressbar.close()
                TARGET_FILE.close()
