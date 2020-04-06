简易中文简繁转换
===============

[文档](https://pythonhosted.org/zhconv/)

**zhconv** 提供基于 MediaWiki 和 OpenCC 词汇表的最大正向匹配简繁转换，支持地区词转换：zh-cn, zh-tw, zh-hk, zh-sg, zh-hans, zh-hant。Python 2、3通用。

若要求高精确度，参见 [OpenCC](https://github.com/BYVoid/OpenCC) 和 [opencc-python](https://pypi.python.org/pypi/opencc-python)。

```pycon
>>> print(convert(u'我幹什麼不干你事。', 'zh-cn'))
我干什么不干你事。
>>> print(convert(u'人体内存在很多微生物', 'zh-tw'))
人體內存在很多微生物
```

其中，zh-hans, zh-hant 仅转换简繁，不转换地区词。

完整支持 MediaWiki 人工转换语法：

```pycon
>>> print(convert_for_mw(u'在现代，机械计算-{}-机的应用已经完全被电子计算-{}-机所取代', 'zh-hk'))
在現代，機械計算機的應用已經完全被電子計算機所取代
>>> print(convert_for_mw(u'-{zh-hant:資訊工程;zh-hans:计算机工程学;}-是电子工程的一个分支，主要研究计算机软硬件和二者间的彼此联系。', 'zh-tw'))
資訊工程是電子工程的一個分支，主要研究計算機軟硬體和二者間的彼此聯繫。
>>> print(convert_for_mw(u'張國榮曾在英國-{zh:利兹;zh-hans:利兹;zh-hk:列斯;zh-tw:里茲}-大学學習。', 'zh-sg'))
张国荣曾在英国利兹大学学习。
>>> print(convert_for_mw('毫米(毫公分)，符號mm，是長度單位和降雨量單位，-{zh-hans:台湾作-{公釐}-或-{公厘}-;zh-hant:港澳和大陸稱為-{毫米}-（台灣亦有使用，但較常使用名稱為毫公分）;zh-mo:台灣作-{公釐}-或-{公厘}-;zh-hk:台灣作-{公釐}-或-{公厘}-;}-。', 'zh-cn'))
毫米(毫公分)，符号mm，是长度单位和降雨量单位，台湾作公釐或公厘。
```

和其他[高级字词转换语法](https://zh.wikipedia.org/wiki/Help:%E9%AB%98%E7%BA%A7%E5%AD%97%E8%AF%8D%E8%BD%AC%E6%8D%A2%E8%AF%AD%E6%B3%95)。

转换字典可下载 [MediaWiki 源码包](https://www.mediawiki.org/wiki/Download)中的 includes/ZhConversion.php，使用 convmwdict.py 可转换成 json 格式。

代码授权协议采用 MIT 协议；转换表由于来自 MediaWiki，为 GPLv2+ 协议。


### 在Spark集群中使用该项目

在分布式集群中，也许受环境限制，不便于在每台机器上安装该项目。
那么你可以从driver机器中单独上传该项目的`egg`文件，不需要依赖于其它的项目。

```
# python setup.py bdist_egg

# ls dist
zhconv-1.2.2-py2.7.egg
```

如果在本地，则可以直接执行`sys.path.append('PATH_TO_ZHCONV/zhconv-1.2.2-py2.7.egg')`后使用。

### 小工具

EPUB 电子书简繁转换：`python3` [epubzhconv.py](https://github.com/The-Orizon/nlputils/blob/master/epubzhconv.py) `输入.epub 输出.epub zh-{cn,tw}`

---

Simple Chinese Conversion Library
=================================

**zhconv** converts between Simplified and Traditional Chinese using maximum forward matching. The conversion table is based on MediaWiki and OpenCC. Supports regional vocabulary: zh-cn, zh-tw, zh-hk, zh-sg, zh-hans, zh-hant. Supports both Python 2 and 3.

Example:

```pycon
>>> print(convert(u'我幹什麼不干你事。', 'zh-cn'))
我干什么不干你事。
>>> print(convert(u'人体内存在很多微生物', 'zh-tw'))
人體內存在很多微生物
```

If zh-hans or zh-hant is used, then regional vocabulary conversion will be disabled.

[Documentation](https://pythonhosted.org/zhconv/) is available in Chinese.

The code is licensed under MIT, while the conversion table is licensed under GPLv2+.
