# Weibo Emoji

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/ArvinZJC/WeiboEmoji?include_prereleases)](https://github.com/ArvinZJC/WeiboEmoji/releases)
[![GitHub All Releases](https://img.shields.io/github/downloads/ArvinZJC/WeiboEmoji/total)](https://github.com/ArvinZJC/WeiboEmoji/releases)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/cc460460e8da4609b40a38532fcb9547)](https://www.codacy.com/gh/ArvinZJC/WeiboEmoji/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ArvinZJC/WeiboEmoji&amp;utm_campaign=Badge_Grade)

**English** | [简体中文](https://github.com/ArvinZJC/WeiboEmoji/blob/master/README-zhCN.md)

Weibo, similar to Twitter, is a Chinese microblogging website launched by Sina. **Weibo Emoji** is a repository for saving and sharing most Emoji images that are used/were previously used by the app Weibo. It contains **389 PNG Emoji images**. There is no best, only better.

## ATTENTION

1. The Emoji images have been sorted out, and they together with the corresponding changelogs can be found in the [Releases](https://github.com/ArvinZJC/WeiboEmoji/releases) section. Please note that these image files should never ever be used for commercial purposes. Just "help yourself" and have fun by, for instance, adding them into your Emoji favourites of chatting apps like WeChat and QQ.
2. The repository has been built based on Weibo Android App V10.11.4 and [Weibo HTML5](https://m.weibo.cn/) V2.4.9.

## Folder Instructions

### [Source1](https://github.com/ArvinZJC/WeiboEmoji/tree/master/Source1)

Once the specified version of Weibo Android App is installed and launched, it will create a data folder to save Emoji resources. The general location is `/storage/emulated/0/sina/weibo/storage/photoalbum_emotion/emotion`. You don't even need the ROOT permission for access. Hence, you can also extract these images on your own. What I have done to save your time is to basically categorise them according to their meanings. The rough time range of this source is from **January 2015 to November 2020**.

Although there are numerous Emoji images, not all of them are shown in the Weibo Emoji list when you use the app. Generally, these images not displayed were previously used to reflect a few hot topics in China Net. I suppose that Weibo might add/replace/remove these image files in a more timely manner.

### [Source2](https://github.com/ArvinZJC/WeiboEmoji/tree/master/Source2)

One part of this folder is Emoji images extracted from the specified resource folder in the corresponding APK file of the app. If you understand the principles of an APK file, it is a piece of cake for you to find these amazing images as well. The image files copied in this way are mostly WEBP ones, which are usually not supported when you want to use them in chatting apps. You can get PNG images by double clicking the BAT file included in this folder to run the script, but it is not recommended. Instead, it is one better choice for you to use file format converters like [Format Factory](http://www.pcgeshi.com/) (~~not AD~~).

It is no doubt that the Emoji images from Source 1 and the resource folder compressed in the APK file are sufficient. However, there are still several fancy and vivid ones that are not included. How to retrieve and download these resources in a relatively simple way became an annoying problem. Fortunately, these kind of images are found on the HTML5 version of Weibo. Hence, thanks to the developer tools of PC's browsers, my solution is to dig for these image files by browsing Weibo HTML5 on Google Chrome. (I don't even know when Google changed the hot key of this feature to `Ctrl` + `Shift` + `I`...)

### [ProcessedImages](https://github.com/ArvinZJC/WeiboEmoji/tree/master/ProcessedImages)

Don't want to convert WEBP images by yourself? Well then, just copy the processed image files from this folder instead of **the corresponding WEBP images** in Source 2.

## Examples

Cracked:

![202011_liekai_mobile.png](./Source1/微博“黄脸”/202011_liekai_mobile.png)

Giving a shoutout:

![moren_dacall_mobile.png](./Source1/微博“黄脸”/moren_dacall_mobile.png)

Ha! Ha!:

![201810_xiaohaha_mobile.png](./Source1/浪小花/201810_xiaohaha_mobile.png)
