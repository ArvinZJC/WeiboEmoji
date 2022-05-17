"""
'''
Description: a Weibo Emoji list data updater
Version: 1.1.0.20220517
Author: Arvin Zhao
Date: 2022-03-22 19:44:09
Last Editors: Arvin Zhao
LastEditTime: 2022-05-17 13:08:43
'''
"""

import json
import os

from onepush import notify

from retriever import retrieve


def notify_tg(is_same: bool) -> None:
    """Notify the Weibo Emoji list data updater's response to a specific Telegram bot.

    Parameters
    ----------
    is_same : bool
        A flag indicating if the data file pending comparison contains the latest data.
    """
    tg_bot_token = os.getenv("TG_BOT_TOKEN")
    tg_user_id = os.getenv("TG_USER_ID")

    if tg_bot_token == None or tg_user_id == None:
        print("No Telegram bot token or user ID found.")
        return

    notify(
        "telegram",
        content="Same data? {}.".format(is_same),
        title="Weibo Emoji Update Checker",
        token=tg_bot_token,
        userid=tg_user_id,
    )


def update(is_fc: bool = False) -> bool:
    """Update the Weibo Emoji list data updater if necessary.

    Parameters
    ----------
    is_fc : bool, optional
        A flag indicating if Aliyun FC is used. Default: `False`.

    Returns
    -------
    bool
        A flag indicating if the data file pending comparison contains the latest data.
    """
    data = retrieve()

    if data is not None:
        data_filename = "weibo-emoji-list.json"
        is_same = False

        if not is_fc and not os.path.exists(data_filename):
            open(data_filename, "w").close()

        with open(data_filename, "r" if is_fc else "r+") as output:
            data_new = json.dumps(data, indent=4)
            data_old = output.read()
            is_same = data_new == data_old

            if not is_same and not is_fc:
                output.seek(0)
                output.write(data_new)
                output.truncate()

        return is_same


# For simple tests only.
if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    notify_tg(update())
