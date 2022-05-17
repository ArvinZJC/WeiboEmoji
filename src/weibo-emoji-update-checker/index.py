"""
'''
Description: the Aliyun FC entry 
Version: 2.0.0.20220517
Author: Arvin Zhao
Date: 2022-03-22 19:18:24
Last Editors: Arvin Zhao
LastEditTime: 2022-05-17 13:07:44
'''
"""

from updater import notify_tg, update


def handler(event: bytes, context: object) -> None:
    """The Aliyun FC's handler.

    Parameters
    ----------
    event : bytes
        The triggered function's basic info.
    context : object (FCContext)
        The context info.
    """
    notify_tg(update(is_fc=True))
