# [WeiboEmoji](../../..)/[src](../)/Weibo Emoji Update Checker

**English (United Kingdom)** | [中文（简体，中国）](./README_zh-Hans-CN.md)

Weibo Emoji Update Checker uses [the `emotions` API](https://open.weibo.com/wiki/2/emotions) officially provided by Weibo to retrieve and store a list of Weibo's Emoji image info in a JSON data file. The file is essential and processed to help generate a new release.

## ❗ ATTENTION

> May I have your attention pls? 🔥

1. By 14 June 2022, everything looks good with Visual Studio Code (Version: 1.68.0) + Python 3.9. The primary packages of the update checker are listed in the following table. For more info, please refer to [`requirements.txt` under the update checker's `src` directory](./src/requirements.txt).

   | Name          | Version |
   | :------------ | :-----: |
   | onepush       |  1.1.1  |
   | python-dotenv | 0.20.0  |

2. You could manually create a file named `.env` under the update checker's root directory and contain the following content. Please note that it is _optional_, and that **the update checker should work well without it**.

   ```sh
   # Set the following environment variables to allow sending messages to your Telegram bot.
   TG_BOT_TOKEN=<your Telegram bot token>
   TG_USER_ID=<your Telegram user ID>

   WB_ACCESS_TOKEN=<your Weibo API access token>  # Set this environment variable to allow retrieving data from Weibo API.
   ```

   You may find the following links useful.

   - [How to create a Telegram bot?](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
   - [How to get the Telegram user ID?](https://bigone.zendesk.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID-)
   - [How to get a Weibo API access token?](https://open.weibo.com/wiki/%E6%8E%88%E6%9D%83%E6%9C%BA%E5%88%B6)

   If all configurations are in place, the script `updater.py` can be executed successfully to generate/update the JSON data file as per the search results.

3. The update checker is designed to deploy on [the Aliyun FC](https://www.aliyun.com/product/fc) to check dialy if any update is available for the stock list. Please note that the package `python-dotenv` is not required in this case, and you need to configure the environment variables in your function configurations. You can refer to [`requirements_fc.txt`](./requirements_fc.txt) to install packages via the online IDE using the following command.

   ```sh
   pip3 install -r requirements_fc.txt -t .
   ```
