# [WeiboEmoji](../../..)/src

[![GitHub](https://img.shields.io/github/license/ArvinZJC/WeiboEmoji)](../LICENCE)

[English (United Kingdom)](./README.md) | **中文（简体，中国）**

`src` 文件夹包含使新版本的打包更方便的工具脚本。这些脚本可被分为如下的 2 部分。

1. 微博表情更新检查器。
2. 用于下载源 1 和处理 2 个源来生成新版本打包的内容的脚本。

更多关于第 1 部分的介绍请参见 [`weibo-emoji-update-checker` 文件夹下的 README](./weibo-emoji-update-checker/README_zh-Hans-CN.md)。至于第 2 部分，其脚本包含 3 个脚本文件——主入口、下载器和用于处理 2 个源的输出生成器。此 README 主要介绍第 2 部分。

## ❗ 注意

> 敲黑板了！敲黑板了！🔥

1. 截至 2023 年 3 月 11 日，使用 Visual Studio Code（版本：1.76.1）和 Python 3.11.1 开发表现良好。第 2 部分主要的包参见下面的表格。更多信息请参见 [`requirements.txt`](./requirements.txt)。

   | 名称          | 版本  |
   | :------------ | :---: |
   | Pillow        | 9.4.0 |
   | python-dotenv | 1.0.0 |

2. 您可以在 `src` 目录下手动创建名为 `.env` 的文件，并包含如下内容。请注意这个操作 _可选_。**在没有这个文件的情况下，此项目应仍能良好运行。**

   ```sh
   VERSION=<新版本的版本号；例如，5.0.0>
   ```
