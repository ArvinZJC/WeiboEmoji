"""
'''
Description: a Weibo Emoji image downloader
Version: 1.0.0.20220325
Author: Arvin Zhao
Date: 2022-03-25 15:08:27
Last Editors: Arvin Zhao
LastEditTime: 2022-03-25 16:41:58
'''
"""

from typing import List
from urllib.request import urlretrieve
import json
import os


def download(ignore_existing: bool = True):
    """Download the Weibo Emoji images from the URLs recorded in the Weibo Emoji list.

    Parameters
    ----------
    ignore_existing : bool
        A flag indicating if the existing image should be redownloaded.
    """
    data_file_path = os.path.join(
        ".", "WeiboEmojiUpdateChecker", "src", "WeiboEmojiList.json"
    )

    if not os.path.exists(data_file_path):
        return

    data_file = open(data_file_path)
    images: List = json.load(data_file)
    data_file.close()

    for image in images:
        category: str = image.get("category")
        directory = os.path.join(
            "..", "img", "source_1", category if category != "" else "默认"
        )
        url: str = image.get("url")
        filename = os.path.join(
            directory, "{}{}".format(image.get("value")[1:-1], url[url.rindex(".") :])
        )

        if os.path.isdir(directory):
            if ignore_existing and os.path.isfile(filename):
                continue
        else:
            os.makedirs(directory)

        urlretrieve(url, filename)


# For simple tests only.
if __name__ == "__main__":
    download()
