![banner.png](./banner.png)

# 微博 Emoji

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/ArvinZJC/WeiboEmoji?include_prereleases)](../../releases)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fa57831c35a64a3d819b15255125d98b)](https://www.codacy.com/gh/ArvinZJC/WeiboEmoji/dashboard?utm_source=github.com&utm_medium=referral&utm_content=ArvinZJC/WeiboEmoji&utm_campaign=Badge_Grade)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ArvinZJC/WeiboEmoji)

[English (United Kingdom)](./README.md) | **中文（简体，中国）**

新浪微博是啥就不用多介绍了哈，我相信能看懂汉字的人基本都知道那货是个啥。**微博 Emoji** 这个“项目”旨在保存并分享微博 app 提供或提供过的大部分 Emoji 表情。它包含 **692 张表情图片**，这可是鄙人悉心整理之作 ~~（往自己脸上贴金）~~。没有最好最全，只有更好更全。不管怎么说，玩儿微博的老铁们不如点点下面的徽章<sup id="source1">[1](#footnote1)</sup>来**加一波关注**？😆

[![微博](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.swo.moe%2Fstats%2Fweibo%2F3218812301&query=count&color=282c34&label=微博&labelColor=e6162d&logo=sina-weibo&suffix=+粉丝&cacheSeconds=3600)](https://weibo.com/3218812301)

## ❗ 注意

> 敲黑板了！敲黑板了！🔥

1. 重要的事情说三遍。禁商！禁商！禁商！您可以将喜欢的表情添加到像微信和 QQ 这样的聊天应用的表情收藏中。您当然还可以向别人疯狂安利哦！👍
2. 在[发行](../../releases)中，您可以找到最新版本更新日志和可下载的 ZIP 文件。这个压缩文件包含 2 个部分——`original` 和 `gif`。前者提供由源 1 和 2 组合得到的 Emoji 表情，后者是为了您的便利由前者转换得到的 GIF 图片<sup id="source2">[2](#footnote2)</sup>。更多关于如何生成这个压缩文件的内容的信息请参见 [`src` 文件夹下的 README](./src/README-zh-Hans-CN.md)。

## 📋 文件夹说明

### [img/source_1](./img/source_1) 🙌

微博 Emoji 在之前有一个方案是通过微博 APK 文件的指定资源文件夹、微博 HTML5 版和微博网页版来提取表情图片的。这通常需要大量的人工操作。因此，这个方案从微博 Emoji 的 V4.0.0 版本开始弃用。

微博官方提供一个 `emotions` 的接口来获取微博表情图片的信息。微博 Emoji 现在利用这个接口来生成源 1。因此，作为**微博 Emoji 的主要源**，源 1 包含了在微博的表情面板中展示的表情图片，并遵循官方记录在微博表情图片信息中的表情分类。

### [img/source_2](./img/source_2) 🧐

如果您喜欢发微博时使用微博的表情，您可能会发现有些表情图片有时是为了体现中国强大的互联网出现的某个热点而加入表情面板的，这些表情图片因其时效性在热乎劲儿过了后就可能被移除。源 2 就是为了尽可能保留这类表情图片。

一种获取这类表情图片的方式是使用安卓版微博。只要您安装并登录使用了最新的安卓版微博，一个存储着 Emoji 资源的文件夹就会出现在您手机存储中。这个文件夹的路径一般是 `/storage/emulated/0/Android/data/com.sina.weibo/files/sina/weibo/storage/photoalbum_emotion/emotion`。您甚至都不需要 ROOT，所以您也完全可以自己提取这些 Emoji。那我有什么用呢？~~（没用）~~ 这里我只不过是使用相应的策略分好了类，兴许能帮您在选择喜欢的表情时省点时间，毕竟时间就是金钱嘛。

### [src](./src) 🚀

新版本的打包在之前需要手动完成一些步骤，这包括但不限于下载源，分类源和转换表情图片至 GIF 格式。这绝对是极其痛苦的。于是我就想，为何不将这些步骤自动化呢？这个想法倒是让我想起了我计算科学硕士毕设导师曾说过的一句话。

> This is what you learn Computing Science for - automation.<sup id="source3">[3](#footnote3)</sup> 👨‍🔧

工具脚本的设计是为了使新版本的打包更方便。请注意这些脚本使用 [GPL-3.0 协议](./LICENCE)。更多信息请参见[此文件夹下的 README](./src/README_zh-Hans-CN.md)。

更多精彩待发现！希望您会爱上她！💖

---

<sub id="footnote1">[1.](#source1) 显示微博粉丝数的徽章由 [Substats](https://github.com/spencerwooo/Substats) 提供技术支持。👍</sub>

<sub id="footnote2">[2.](#source2) GIF 图片似有更好的显示效果，尤其是将表情添加到微信（iPhone/iPad 版）和 QQ 中的表情收藏中。</sub>

<sub id="footnote3">[3.](#source3) 别抬杠！这句话是有上下文的。</sub>
