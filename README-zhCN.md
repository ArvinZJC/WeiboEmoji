# 微博Emoji

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/ArvinZJC/WeiboEmoji?include_prereleases)](https://github.com/ArvinZJC/WeiboEmoji/releases)
[![GitHub All Releases](https://img.shields.io/github/downloads/ArvinZJC/WeiboEmoji/total)](https://github.com/ArvinZJC/WeiboEmoji/releases)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/cc460460e8da4609b40a38532fcb9547)](https://www.codacy.com/gh/ArvinZJC/WeiboEmoji/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ArvinZJC/WeiboEmoji&amp;utm_campaign=Badge_Grade)

[English](https://github.com/ArvinZJC/WeiboEmoji/blob/master/README.md) | **简体中文**

新浪微博是啥就不用多介绍了哈，我相信能看懂汉字的人基本都知道那货是个啥。**微博Emoji**这个“项目”旨在保存并分享微博app提供或提供过的大部分Emoji表情。它包含**401张PNG格式的表情图片**，这可是鄙人悉心整理之作（~~往自己脸上贴金~~）。没有最好最全，只有更好更全。

## 注意

1. Emoji表情已经过整理，它们和相应的更新日志可在[发行](https://github.com/ArvinZJC/ShSzStockHelper-Windows/releases)部分找到。重要的事情说三遍。禁商！禁商！禁商！我很乐意您可以尽情将您喜欢的表情添加到像微信和QQ这样的聊天应用的表情收藏中。
2. 资源基于微博安卓app V10.12.4和[微博HTML5](https://m.weibo.cn/) V2.4.9.

## 文件夹说明

### [Source1](https://github.com/ArvinZJC/WeiboEmoji/tree/master/Source1)

微博这些精美的表情图片其实没有那么难获取啦。不知道从哪个版本开始，只要您安装使用了微博安卓app，一个存储着Emoji资源的文件夹就会出现在您手机存储中。这个文件夹的路径一般是`/storage/emulated/0/sina/weibo/storage/photoalbum_emotion/emotion`。您甚至都不需要ROOT，所以您也完全可以自己提取这些Emoji。那我有什么用呢？（~~没用~~）这里我只不过是分好了类，兴许能帮您在选择喜欢的表情时省点时间，毕竟时间就是金钱嘛。这些Emoji的时间范围大致是**从2015年1月到2020年12月**。

您可能会寻思：这微博app里也没这么多表情啊？的确，这些表情并不会都出现在微博app的表情列表里（但是没出现的依然会占用您的手机存储空间）。一般地，这些没出现的“时效性”的表情是曾经用来体现中国强大的互联网出现的某个热点的，热点过了自然就应该被替换了。

### [Source2](https://github.com/ArvinZJC/WeiboEmoji/tree/master/Source2)

这个文件夹中的表情图片一部分提取自微博app的APK文件。若您了解APK文件的真面目，提取这部分表情图片就是小菜一碟。不过呢，这种方式提取到的图片多为WEBP格式的。想要在聊天应用中使用它们可能需要转换格式。在Windows上，您可双击运行此文件夹中的BAT脚本文件轻松获得对应的PNG格式的表情图片。什么？哪个BAT？拜托，有且仅有一个BAT文件啦。需要注意的是，我不建议您通过这种方式转换格式，使用格式转换工具更保险哦，比如[格式工厂](http://www.pcgeshi.com/)（~~并不是广告~~）。

毫无疑问，Source 1和从APK文件提取到的表情图片已经挺多的了。这就满足了？事实上，仍有我见过的一些生动形象的表情没有囊括其中。怎么比较简单又能保证质量地获取到它们有幸是我漫长TODO清单里的一个任务。幸运的是，我在网上瞎冲浪的时候发现了微博HTML5版，上面正有我寻找的那些表情。于是，我借助Google Chrome的开发者工具（鬼知道啥时候谷歌把这个功能的快捷键改成了`Ctrl` + `Shift` + `I`，我咋记得以前是`F12`）成功从相应的图片网址上下载下这些表情图片。也不是啥高技术含量的操作，但就是有一种挖到宝的感觉，有木有？

### [ProcessedImages](https://github.com/ArvinZJC/WeiboEmoji/tree/master/ProcessedImages)

嫌转换WEBP格式的图片太麻烦？亲，您可真是个小懒蛋呢，不过没有关系，我帮您转换好了，都在这个文件夹了，在Source 2中**对应的WEBP格式的图片**您可以不用拷贝了。

## 样例

裂开:

![202011_liekai_mobile.png](./Source1/微博“黄脸”/202011_liekai_mobile.png)

打call:

![moren_dacall_mobile.png](./Source1/微博“黄脸”/moren_dacall_mobile.png)

浪小花-笑哈哈:

![201810_xiaohaha_mobile.png](./Source1/浪小花/201810_xiaohaha_mobile.png)
