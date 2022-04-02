"""
'''
Description: a Weibo Emoji image downloader
Version: 1.0.0.20220401
Author: Arvin Zhao
Date: 2022-03-25 15:08:27
Last Editors: Arvin Zhao
LastEditTime: 2022-04-01 20:35:17
'''
"""

from typing import Dict, List, Optional
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
    print("Downloading Weibo Emoji images...")
    images = load_emoji_list()

    for image in images:
        category: str = image.get("category", "未定义")
        category_dir = os.path.join(
            "..", "img", "source_1", category if category != "" else "默认"
        )
        url: Optional[str] = image.get("url")
        value: Optional[str] = image.get("value")

        if url is None or value is None:
            print("No URL or value found in the image dict {}.".format(image))
            continue

        filename = os.path.join(
            category_dir, "{}{}".format(value[1:-1], url[url.rindex(".") :])
        )

        if os.path.isdir(category_dir):
            if ignore_existing and os.path.isfile(filename):
                continue
        else:
            os.makedirs(category_dir)

        urlretrieve(url, filename)


def load_emoji_list() -> List[Dict]:
    """Load the Weibo Emoji list.

    Returns
    -------
    List[Dict]
        The Weibo Emoji list.
    """
    data_file_path = os.path.join(
        ".", "WeiboEmojiUpdateChecker", "src", "WeiboEmojiList.json"
    )

    if not os.path.exists(data_file_path):
        print("No Weibo Emoji list found.")
        return []

    data_file = open(data_file_path)
    images: List[Dict] = json.load(data_file)
    data_file.close()
    return images


# For simple tests only.
if __name__ == "__main__":
    download()
