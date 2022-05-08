# [WeiboEmoji](../../..)/[src](../)/微博表情更新检查器

[English](./README.md) | **简体中文**

微博更新检查器使用微博官方提供的 [`emotions` 接口](https://open.weibo.com/wiki/2/emotions)来查询微博表情图片信息，并将它们保存在一个 JSON 数据文件中。这个数据文件是用来帮助打包新版本必不可少的数据来源。

## ❗ 注意

> 敲黑板了！敲黑板了！🔥

1. 截至 2022 年 5 月 8 日，使用 Visual Studio Code（版本：1.67.0）和 Python 3.6 开发表现良好。此更新检查器主要的包参见下面的表格。更多信息请参见[在更新检查器的 `src` 目录下的 `requirements.txt`](./src/requirements.txt)。

   | 名称          |  版本  |
   | :------------ | :----: |
   | onepush       | 1.1.1  |
   | python-dotenv | 0.20.0 |

2. 您可以在此更新检查器的 `src` 目录下手动创建名为 `.env` 的文件，并包含如下内容。请注意这个操作 _可选_。**在没有这个文件的情况下，此项目应仍能良好运行**。

   ```sh
   # 设定如下环境变量来允许发送消息到您的 Telegram 机器人。
   TG_BOT_TOKEN=<您的 Telegram 机器人 token 凭证>
   TG_USER_ID=<您的 Telegram 用户 ID>

   WB_ACCESS_TOKEN=<您用于访问微博开发者接口的 token 凭证>  # 设定此环境变量来允许通过微博的接口查询数据。
   ```

   您也许会觉得下面的链接比较有用。

   - [如何创建一个 Telegram 机器人？](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
   - [如何获取 Telegram 用户 ID？](https://bigone.zendesk.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID-)
   - [如何获取用于访问微博开发者接口的 token 凭证？](https://open.weibo.com/wiki/%E6%8E%88%E6%9D%83%E6%9C%BA%E5%88%B6)

   若一切配置妥当，则应可成功执行在更新检查器的 `src` 目录下的 `updater.py` 脚本来根据查询结果生成/更新 JSON 数据文件。

3. 此更新检查器被设计用来部署在[腾讯云函数](https://cloud.tencent.com/product/scf)上去检查股票列表是否有更新。为了部署方便，配置文件模板提供如下。如果您想，您可以参考[腾讯云函数相关的官方文档](https://cloud.tencent.com/document/product/583/44751)来使用它。

   ```YAML
   app: WeiboEmojiUpdateChecker
   component: scf
   inputs:
   description: My Weibo Emoji update checker.
   eip: false
   # environment:
      # variables:
         # TG_BOT_TOKEN: <您的 Telegram 机器人 token 凭证>
         # TG_USER_ID: <您的 Telegram 用户 ID>
         # WB_ACCESS_TOKEN: <您用于访问微博开发者接口的 token 凭证>
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
   # 在使用此配置文件部署时，请确保文件名为 “serverless.yaml”。
   # 更多信息参见: https://github.com/serverless-components/tencent-scf/blob/master/docs/configure.md
   ```
