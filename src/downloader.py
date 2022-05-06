"""
'''
Description: a Weibo Emoji image downloader
Version: 1.0.4.20220506
Author: Arvin Zhao
Date: 2022-03-25 15:08:27
Last Editors: Arvin Zhao
LastEditTime: 2022-05-06 14:38:40
'''
"""

from typing import Dict, List, Optional
from urllib.parse import quote
from urllib.request import urlretrieve
import json
import os
import shutil

ERROR_MESSAGE_TEMPLATE = "Error: {}"


def download() -> None:
    """Download the Weibo Emoji images from the URLs recorded in the Weibo Emoji list."""
    print("Downloading Weibo Emoji images...")
    images = load_emoji_list()
    source_1_dir = os.path.join("..", "img", "source_1")

    if os.path.isdir(source_1_dir):
        try:
            shutil.rmtree(source_1_dir)
        except OSError as e:
            print(ERROR_MESSAGE_TEMPLATE.format(e))
            return

    for image in images:
        category: str = image.get("category", "未定义")
        category_dir = os.path.join(source_1_dir, category if category != "" else "默认")
        url: Optional[str] = image.get("url")
        value: Optional[str] = image.get("value")

        if url is None or value is None:
            print("No URL or value found in the image dict {}.".format(image))
            continue

        if not os.path.isdir(category_dir):
            os.makedirs(category_dir)

        urlretrieve(
            quote(url, safe=":/"),
            os.path.join(
                category_dir, "{}{}".format(value[1:-1], url[url.rindex(".") :])
            ),
        )


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
