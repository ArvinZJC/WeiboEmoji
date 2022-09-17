# [WeiboEmoji](../../..)/src

[![GitHub](https://img.shields.io/github/license/ArvinZJC/WeiboEmoji)](../LICENCE)

**English (United Kingdom)** | [中文（简体，中国）](./README_zh-Hans-CN.md)

The `src` folder contains the helper scripts to make it more convenient to generate a new release. These scripts can be divided into 2 parts as follows.

1. Weibo Emoji Update Checker.
2. The scripts to download Source 1 and process both sources to generate the content for a new release.

For more info about Part 1, please refer to [the README file in the folder `weibo-emoji-update-checker`](./weibo-emoji-update-checker/README.md). As for Part 2, the scripts contain 3 script files - the main entry, the downloader, and the output generator to process both sources. This README file primarily introduces Part 2.

## ❗ ATTENTION

> May I have your attention pls? 🔥

1. By 17 September 2022, everything looks good with Visual Studio Code (Version: 1.71.2) + Python 3.10.6. The primary packages of Part 2 are listed in the following table. For more info, please refer to [`requirements.txt`](./requirements.txt).

   | Name          | Version |
   | :------------ | :-----: |
   | Pillow        |  9.2.0  |
   | python-dotenv | 0.21.0  |

2. You could manually create a file named `.env` under the `src` directory and contain the following content. Please note that it is _optional_, and that **the project should work well without it**.

   ```sh
   VERSION=<the version of the new release; e.g., 4.0.0>
   ```
