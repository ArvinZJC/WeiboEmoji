![banner.png](./banner.png)

# Weibo Emoji

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/ArvinZJC/WeiboEmoji?include_prereleases)](../../releases)
[![GitHub All Releases](https://img.shields.io/github/downloads/ArvinZJC/WeiboEmoji/total)](../../releases)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fa57831c35a64a3d819b15255125d98b)](https://www.codacy.com/gh/ArvinZJC/WeiboEmoji/dashboard?utm_source=github.com&utm_medium=referral&utm_content=ArvinZJC/WeiboEmoji&utm_campaign=Badge_Grade)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ArvinZJC/WeiboEmoji)
![GitHub](https://img.shields.io/github/license/ArvinZJC/WeiboEmoji)

**English** | [简体中文](./README-zhCN.md)

Weibo, similar to Twitter, is a Chinese microblogging website launched by Sina. **Weibo Emoji** is a repository for saving and sharing most Emoji images that are used/were previously used by the app Weibo. It contains **457 different Emoji images**. There is no best, only better. So do you use Weibo? If yes, why not click the following badge<sup id="source1">[1](#footnote1)</sup> and **follow me now**? 😆

[![Weibo](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.swo.moe%2Fstats%2Fweibo%2F3218812301&query=count&color=282c34&label=Weibo&labelColor=e6162d&logo=sina-weibo&suffix=+followers&cacheSeconds=3600)](https://weibo.com/3218812301)

## ❗ ATTENTION

> May I have your attention pls? 🔥

1. The repository has been built based on Weibo for Android V11.9.2, [Weibo Web](https://weibo.com/), and [Weibo HTML5](https://m.weibo.cn/) V2.9.12.
2. These Emoji images should never ever be used for commercial purposes. You could add them into your Emoji favourites of chatting apps like WeChat and QQ. You could recommend them to others, and then you deserve a thumb-up. 👍
3. For each version, you could find the changelog and a ZIP file for downloading in the [Releases](../../releases) section. The ZIP file contains the Emoji images sorted out and converted to GIF images<sup id="source2">[2](#footnote2)</sup> for you.

## 📋 Folder Instructions

### [Images/Source1](./Images/Source1): 🙌

Once the specified version of Weibo for Android is installed, launched, and has a user logged in, it will save Emoji resources in its app data folder. The general location is `/storage/emulated/0/Android/data/com.sina.weibo/files/sina/weibo/storage/photoalbum_emotion/emotion`. You do not even need the ROOT permission for access. Hence, you can also extract these images on your own. What I have done to save your time is to basically categorise them according to their meanings. The rough time range of this source is from **January 2015 to September 2021**.

Although there are numerous Emoji images, not all of them are shown in the Weibo Emoji list when you use the app. Generally, these images not displayed were previously used to reflect a few hot topics in China Net. Weibo might add/replace/remove these image files in a more timely manner.

### [Images/Source2](./Images/Source2): 🧐

One part of this folder is Emoji images extracted from the specified resource folder (`/res/drawable-xxhdpi-v4`) in the corresponding APK file of the app. If you understand the principles of an APK file, it is a piece of cake for you to find these amazing images as well. Please note that the image files copied in this way are **mostly WEBP ones**, which are usually not supported when you want to use them in chatting apps.

It is no doubt that the Emoji images from Source 1 and the resource folder compressed in the APK file are sufficient. However, there are still several fancy and vivid ones that are not included. How to retrieve and download these resources in a relatively simple way became an annoying problem. Fortunately, these kind of images are found on Weibo Web and Weibo HTML5. Hence, thanks to the developer tools of PC's browsers, a feasible solution is to dig for these image files by browsing the web pages on Google Chrome.

### [Scripts](./Scripts): 🚀

The helper scripts are designed to make it more convenient to generate a new release. Please note that the code is licensed under [the GPL-3.0 License](./LICENSE). For more information, please refer to [the README file in this folder](./Scripts/README.md).

> 📢 Refactoring was planned at the time releasing V3.6.0. The innovative V4.0.0 is on its way to bring you the brand-new magic.

## 💥 Examples

|                                       Image                                       |      Meaning      |
| :-------------------------------------------------------------------------------: | :---------------: |
|   ![2021_bitter_mobile.png](./Images/Source1/微博“黄脸”/2021_bitter_mobile.png)   |      Bitter       |
| ![202011_liekai_mobile.png](./Images/Source1/微博“黄脸”/202011_liekai_mobile.png) |      Cracked      |
|  ![moren_dacall_mobile.png](./Images/Source1/微博“黄脸”/moren_dacall_mobile.png)  | Giving a shoutout |
|     ![2018_doge_mobile.png](./Images/Source1/微博“黄脸”/2018_doge_mobile.png)     |       Doge        |
|  ![2021_alongdog_org.png](./Images/Source1/两大虐狗节/2021_alongdog_mobile.png)   |    Damn single    |
|    ![dorachijing_mobile.png](./Images/Source1/哆啦A梦/dorachijing_mobile.png)     |      Shocked      |

There is much more for you to explore. Hope you will enjoy it. 💖

---

<sub id="footnote1">[1.](#source1) The badge showing the number of followers on Weibo is powered by [Substats](https://github.com/spencerwooo/Substats). 👍</sub>

<sub id="footnote2">[2.](#source2) It has been proved that GIF images could have better compatibility, especially with WeChat (for iPhone/iPad) and QQ, when adding to the Emoji favourites.</sub>
