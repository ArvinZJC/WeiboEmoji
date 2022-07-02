# [WeiboEmoji](../../..)/[src](../)/微博表情更新检查器

[English (United Kingdom)](./README.md) | **中文（简体，中国）**

微博表情更新检查器使用微博官方提供的 [`emotions` 接口](https://open.weibo.com/wiki/2/emotions)来查询微博表情图片信息，并将它们保存在一个 JSON 数据文件中。这个数据文件是用来帮助打包新版本必不可少的数据来源。

## ❗ 注意

> 敲黑板了！敲黑板了！🔥

1. 截至 2022 年 7 月 2 日，使用 Visual Studio Code（版本：1.68.1）和 Python 3.9 开发表现良好。此更新检查器主要的包参见下面的表格。更多信息请参见[在更新检查器的 `src` 目录下的 `requirements.txt`](./src/requirements.txt)。

   | 名称          |  版本  |
   | :------------ | :----: |
   | onepush       | 1.1.1  |
   | python-dotenv | 0.20.0 |

2. 您可以在此更新检查器的根目录下手动创建名为 `.env` 的文件，并包含如下内容。请注意这个操作 _可选_。**在没有这个文件的情况下，此更新检查器应仍能良好运行**。

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

   若一切配置妥当，则应可成功执行 `updater.py` 脚本来根据查询结果生成/更新 JSON 数据文件。

3. 此更新检查器被设计用来部署在[阿里云函数计算 FC](https://www.aliyun.com/product/fc) 上来每日检查股票列表是否有更新。请注意此时 `python-dotenv` 包不再需要，并且您需要在您的韩束配置中配置环境变量。您可参见 [`requirements_fc.txt`](./requirements_fc.txt) 来通过在线 IDE 使用如下命令安装包。

   ```sh
   pip3 install -r requirements_fc.txt -t .
   ```
