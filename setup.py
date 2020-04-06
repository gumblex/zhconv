#-*- coding: UTF-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

LONGDESC = '''
简易中文简繁转换
==================================

**zhconv** 提供基于 MediaWiki 词汇表的最大正向匹配简繁转换。Python 2, 3 通用。支持以下地区词转换：

* ``zh-cn`` 大陆简体
* ``zh-tw`` 台灣正體
* ``zh-hk`` 香港繁體
* ``zh-sg`` 马新简体（无词汇表，需要手工指定）
* ``zh-hans`` 简体
* ``zh-hant`` 繁體

示例
----

.. code-block:: pycon

   >>> print(convert(u'我幹什麼不干你事。', 'zh-cn'))
   我干什么不干你事。
   >>> print(convert(u'人体内存在很多微生物', 'zh-tw'))
   人體內存在很多微生物

完整支持 MediaWiki 人工转换语法：

.. code-block:: pycon

   >>> print(convert_for_mw(u'在现代，机械计算-{}-机的应用已经完全被电子计算-{}-机所取代', 'zh-hk'))
   在現代，機械計算機的應用已經完全被電子計算機所取代
   >>> print(convert_for_mw(u'-{zh-hant:資訊工程;zh-hans:计算机工程学;}-是电子工程的一个分支，主要研究计算机软硬件和二者间的彼此联系。', 'zh-tw'))
   資訊工程是電子工程的一個分支，主要研究計算機軟硬體和二者間的彼此聯繫。
   >>> print(convert_for_mw(u'張國榮曾在英國-{zh:利兹;zh-hans:利兹;zh-hk:列斯;zh-tw:里茲}-大学學習。', 'zh-sg'))
   张国荣曾在英国利兹大学学习。
   >>> print(convert_for_mw('毫米(毫公分)，符號mm，是長度單位和降雨量單位，-{zh-hans:台湾作-{公釐}-或-{公厘}-;zh-hant:港澳和大陸稱為-{毫米}-（台灣亦有使用，但較常使用名稱為毫公分）;zh-mo:台灣作-{公釐}-或-{公厘}-;zh-hk:台灣作-{公釐}-或-{公厘}-;}-。', 'zh-cn'))
   毫米(毫公分)，符号mm，是长度单位和降雨量单位，台湾作公釐或公厘。

和其他 `高级字词转换语法 <https://zh.wikipedia.org/wiki/Help:%E9%AB%98%E7%BA%A7%E5%AD%97%E8%AF%8D%E8%BD%AC%E6%8D%A2%E8%AF%AD%E6%B3%95>`_。

命令行工具
----------

::

   python -mzhconv [-w] {zh-cn|zh-tw|zh-hk|zh-sg|zh-hans|zh-hant|zh} < input > output
'''

setup(
    name='zhconv',
    version='1.4.1',
    description="A simple implementation of Simplified-Traditional Chinese conversion.",
    long_description=LONGDESC,
    author='Dingyuan Wang',
    author_email='abcdoyle888@gmail.com',
    license='GPLv2+',
    packages=['zhconv'],
    package_data={'zhconv': ['*.json']},
    platforms='any',
    keywords='chinese conversion',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    url='https://github.com/gumblex/zhconv'
)
