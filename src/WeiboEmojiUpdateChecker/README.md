# [WeiboEmoji](../../..)/[src](../)/Weibo Emoji Update Checker

**English** | [简体中文](./README_zhCN.md)

Weibo Emoji Update Checker uses [the `emotions` API](https://open.weibo.com/wiki/2/emotions) officially provided by Weibo to retrieve and store a list of Weibo's Emoji image info in a JSON data file. The file is essential and processed to help generate a new release.

## ❗ ATTENTION

> May I have your attention pls? 🔥

1. By 6 May 2022, everything looks good with Visual Studio Code (Version: 1.67.0) + Python 3.6. The primary packages of the update checker are listed in the following table. For more info, please refer to [`requirements.txt` under the update checker's `src` directory](./src/requirements.txt).

   | Name          | Version |
   | :------------ | :-----: |
   | onepush       |  1.1.1  |
   | python-dotenv | 0.20.0  |

2. You could manually create a file named `.env` under the update checker's `src` directory and contain the following content. Please note that it is _optional_, and that **the project should work well without it**.

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

   If all configurations are in place, the script `updater.py` under the update checker's `src` directory can be executed successfully to generate/update the JSON data file as per the search results.

3. The update checker is designed to deploy on [Tencent SCF](https://cloud.tencent.com/product/scf) to check if any update is available for the Weibo Emoji list. A configuration file template is provided as follows for deployment convenience. You may refer to [the relevant official documents of Tencent SCF](https://cloud.tencent.com/document/product/583/44751) to use it if you want.

   ```YAML
   app: WeiboEmojiUpdateChecker
   component: scf
   inputs:
   description: My Weibo Emoji update checker.
   eip: false
   # environment:
      # variables:
         # TG_BOT_TOKEN: <your Telegram bot token>
         # TG_USER_ID: <your Telegram user ID>
         # WB_ACCESS_TOKEN: <your Weibo API access token>
   events:
      - timer:
         parameters:
            cronExpression: 0 0 6 * * * *
            enable: true
            qualifier: $DEFAULT
   handler: index.main_handler
   initTimeout: 65
   memorySize: 128
   msgTTL: 21600
   name: StockListUpdateChecker
   namespace: default
   publicAccess: true
   region: ap-hongkong
   retryNum: 2
   runtime: Python3.6
   src:
      exclude:
         - '.env'
         - '__pycache__'
      src: ./src
   timeout: 3
   type: event
   name: ap-hongkong_default_StockListUpdateChecker
   stage: dev
   # When using this configuration file for deployment, make sure the file name is "serverless.yaml".
   # For more info: https://github.com/serverless-components/tencent-scf/blob/master/docs/configure.md
   ```
