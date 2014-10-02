简易中文简繁转换
===============

**zhconv** 提供基于 MediaWiki 词汇表的最大正向匹配简繁转换，支持地区词转换：zh-cn, zh-tw, zh-hk, zh-sg, zh-hans, zh-hant。Python 2、3通用。

做这个主要是因为用于 Python 的中文简繁转换很少。[langconv](https://github.com/skydark/nstools/blob/master/zhtools/langconv.py)算一个，还有 [Pyzh](https://code.google.com/p/pyzh/)等。langconv 太复杂，而且不支持地区词转换；Pyzh 太简单，只支持字对字。

[OpenCC](https://github.com/BYVoid/OpenCC) 和 [opencc-python](https://pypi.python.org/pypi/opencc-python) 是一个比较完整准确的解决方案，但不适合纯 Python 环境和对精确度要求不高的需要。

```pycon
>>> print(convert(u'我幹什麼不干你事。', 'zh-cn'))
我干什么不干你事。
>>> print(convert(u'人体内存在很多微生物', 'zh-tw'))
人體內存在很多微生物
```

支持 MediaWiki 人工转换语法：

```pycon
>>> print(convert_for_mw(u'在现代，机械计算-{}-机的应用已经完全被电子计算-{}-机所取代', 'zh-hk'))
在現代，機械計算機的應用已經完全被電子計算機所取代
>>> print(convert_for_mw(u'-{zh-hant:資訊工程;zh-hans:计算机工程学;}-是电子工程的一个分支，主要研究计算机软硬件和二者间的彼此联系。', 'zh-tw'))
資訊工程是電子工程的一個分支，主要研究計算機軟硬體和二者間的彼此聯繫。
>>> print(convert_for_mw(u'張國榮曾在英國-{zh:利兹;zh-hans:利兹;zh-hk:列斯;zh-tw:里茲}-大学學習。', 'zh-sg'))
张国荣曾在英国利兹大学学习。
```

转换字典可下载 includes/ZhConversion.php，使用 convmwdict.py 可转换成 json 格式。

授权协议采用 MIT 协议。

