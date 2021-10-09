![banner.png](./banner.png)

# 微博 Emoji

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/ArvinZJC/WeiboEmoji?include_prereleases)](../../releases)
[![GitHub All Releases](https://img.shields.io/github/downloads/ArvinZJC/WeiboEmoji/total)](../../releases)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fa57831c35a64a3d819b15255125d98b)](https://www.codacy.com/gh/ArvinZJC/WeiboEmoji/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ArvinZJC/WeiboEmoji&amp;utm_campaign=Badge_Grade)
![GitHub](https://img.shields.io/github/license/ArvinZJC/WeiboEmoji)

[English](./README.md) | **简体中文**

新浪微博是啥就不用多介绍了哈，我相信能看懂汉字的人基本都知道那货是个啥。**微博 Emoji** 这个“项目”旨在保存并分享微博 app 提供或提供过的大部分 Emoji 表情。它包含**457张不同的表情图片**，这可是鄙人悉心整理之作 ~~（往自己脸上贴金）~~。没有最好最全，只有更好更全。不管怎么说，玩儿微博的老铁们不如点点下面的徽章<sup id="source1">[1](#footnote1)</sup>来**加一波关注**？😆

[![Weibo](https://img.shields.io/badge/dynamic/json?logo=sina-weibo&label=微博粉丝&color=ff8200&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dweibo%26queryKey%3D3218812301&longCache=true)](https://weibo.com/u/3218812301)

## ❗ 注意

> 敲黑板了！敲黑板了！🔥

1. 资源基于安卓版微博 V11.9.2、[微博网页版](https://weibo.com/)和[微博 HTML5](https://m.weibo.cn/) V2.9.12.
2. 重要的事情说三遍。禁商！禁商！禁商！您可以将喜欢的表情添加到像微信和 QQ 这样的聊天应用的表情收藏中。您当然还可以向别人疯狂安利哦！👍
3. 在[发行](../../releases)部分，您可以找到版本更新日志和可下载的 ZIP 文件。这个压缩文件包含所有 Emoji 表情，并经过整理、转换成 GIF 格式<sup id="source2">[2](#footnote2)</sup>。

## 📋 文件夹说明

### [Images/Source1](./Images/Source1): 🙌

微博这些精美的表情图片其实没有那么难获取啦。不知道从哪个版本开始，只要您安装并登录使用了安卓版微博，一个存储着 Emoji 资源的文件夹就会出现在您手机存储中。这个文件夹的路径一般是 `/storage/emulated/0/Android/data/com.sina.weibo/files/sina/weibo/storage/photoalbum_emotion/emotion`。您甚至都不需要 ROOT，所以您也完全可以自己提取这些 Emoji。那我有什么用呢？~~（没用）~~ 这里我只不过是分好了类，兴许能帮您在选择喜欢的表情时省点时间，毕竟时间就是金钱嘛。这些 Emoji 的时间范围大致是**从2015年1月到2021年9月**。

您可能会寻思：这微博里也没这么多表情啊？的确，这些表情并不会都出现在微博的表情列表里（但是没出现的依然能占用您的手机存储空间）。一般地，这些没出现的“时效性”的表情是曾经用来体现中国强大的互联网出现的某个热点的，热乎劲儿过了就被替换了。

### [Images/Source2](./Images/Source2): 🧐

这个文件夹中的表情图片一部分提取自安卓版微博 APK 文件的指定资源文件夹（`/res/drawable-xxhdpi-v4`）。若您了解 APK 文件的真面目，提取这部分表情图片就是小菜一碟。不过呢，这种方式提取到的图片**多为 WEBP 格式的**。想要在聊天应用中使用它们一般需要转换格式。

毫无疑问，Source 1和从 APK 文件提取到的表情图片已经挺多的了。这就满足了？事实上，仍有我见过的一些生动形象的表情没有囊括其中。怎么比较简单又能保证质量地获取到它们有幸是我漫长 TODO 清单里的一个任务。幸运的是，我在网上瞎冲浪的时候发现了微博网页版和微博 HTML5 版，上面正有我寻找的那些表情。于是，一种可行的办法是借助 Google Chrome 的开发者工具从相应的图片网址上下载这些表情图片。也不是啥高技术含量的操作，但就是有一种挖到宝的感觉，有木有？

### [Scripts](./Scripts): 🚀

工具脚本的设计是为了使新版本的打包更方便。请注意此项目使用 [GPL-3.0 协议](./LICENSE)。更多信息请参见[此文件夹下的 README](./Scripts/README_zhCN.md)。

> 📢 重构在发布 V3.6.0 的时候已提上日程。船新的 V4.0.0 正在悄默默地准备给您一个惊喜。

## 💥 样例

| 表情 | 释义 |
| :--: | :--: |
| ![2021_bitter_mobile.png](./Images/Source1/微博“黄脸”/2021_bitter_mobile.png) | 苦涩 |
| ![202011_liekai_mobile.png](./Images/Source1/微博“黄脸”/202011_liekai_mobile.png) | 裂开 |
| ![2018_doge_mobile.png](./Images/Source1/微博“黄脸”/2018_doge_mobile.png) | Doge（~~不是狗狗币~~） |
| ![moren_dacall_mobile.png](./Images/Source1/微博“黄脸”/moren_dacall_mobile.png) | 打 call |
| ![2021_alongdog_org.png](./Images/Source1/两大虐狗节/2021_alongdog_mobile.png) | 单身狗 |
| ![dorachijing_mobile.png](./Images/Source1/哆啦A梦/dorachijing_mobile.png) | 震惊 |

更多精彩待发现！希望您会爱上她！💖

****

<sub id="footnote1">[1.](#source1) 显示微博粉丝数的徽章由 [Substats](https://github.com/spencerwooo/Substats) 提供技术支持。👍</sub>

<sub id="footnote2">[2.](#source2) GIF 图片经证明能有更好的显示效果，尤其是将表情添加到微信（iPhone/iPad 版）和 QQ 中的表情收藏中。</sub>
