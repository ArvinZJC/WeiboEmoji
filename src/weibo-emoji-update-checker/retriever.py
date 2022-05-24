"""
'''
Description: a Weibo Emoji list raw data retriever
Version: 1.0.2.20220524
Author: Arvin Zhao
Date: 2022-03-22 19:50:51
Last Editors: Arvin Zhao
LastEditTime: 2022-05-24 12:41:35
'''
"""

from typing import Optional
from urllib.request import urlopen
import json
import os


def retrieve() -> Optional[list]:
    """Retrieve the Weibo Emoji list raw data retriever.

    Returns
    -------
    List / None
        The Weibo Emoji list raw data. Return null if the Weibo access token is not provided.
    """
    wb_access_token = os.getenv("WB_ACCESS_TOKEN")

    if wb_access_token == None:
        print("No Weibo access token found.")
        return None

    return json.loads(
        urlopen(
            "https://api.weibo.com/2/emotions.json?access_token={}".format(
                wb_access_token
            )
        ).read()
    )


# For simple tests only.
if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    print(len(retrieve()))
