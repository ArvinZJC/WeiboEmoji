"""
'''
Description: a Weibo Emoji list raw data retriever
Version: 1.0.0.20220325
Author: Arvin Zhao
Date: 2022-03-22 19:50:51
Last Editors: Arvin Zhao
LastEditTime: 2022-03-25 13:18:49
'''
"""

from typing import List, Optional
from urllib.request import urlopen
import json
import os


def retrieve() -> Optional[List]:
    """Retrieve the Weibo Emoji list raw data retriever.

    Returns
    -------
    List / None
        The Weibo Emoji list raw data. Return null if the Weibo access token is not provided.
    """
    wb_access_token = os.getenv("WB_ACCESS_TOKEN")

    if wb_access_token == None:
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
