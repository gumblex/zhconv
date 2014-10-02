#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module implements a simple conversion and localization between simplified and traditional Chinese using tables from MediaWiki.
It doesn't contains a segmentation function and uses maximal forward matching, so it's simple.
For a complete and accurate solution, see OpenCC.
For Chinese segmentation, see Jieba.

    >>> print(convert(u'我幹什麼不干你事。', 'zh-cn'))
    我干什么不干你事。
    >>> print(convert(u'人体内存在很多微生物', 'zh-tw'))
    人體內存在很多微生物

Support MediaWiki's convertion format:

    >>> print(convert_for_mw(u'在现代，机械计算-{}-机的应用已经完全被电子计算-{}-机所取代', 'zh-hk'))
    在現代，機械計算機的應用已經完全被電子計算機所取代
    >>> print(convert_for_mw(u'-{zh-hant:資訊工程;zh-hans:计算机工程学;}-是电子工程的一个分支，主要研究计算机软硬件和二者间的彼此联系。', 'zh-tw'))
    資訊工程是電子工程的一個分支，主要研究計算機軟硬體和二者間的彼此聯繫。
    >>> print(convert_for_mw(u'張國榮曾在英國-{zh:利兹;zh-hans:利兹;zh-hk:列斯;zh-tw:里茲}-大学學習。', 'zh-sg'))
    张国荣曾在英国利兹大学学习。

"""
import os
import sys
import json
from functools import wraps

locales = {
    'zh-cn': ('zh-cn', 'zh-hans', 'zh'),
    'zh-hk': ('zh-hk', 'zh-hant', 'zh'),
    'zh-tw': ('zh-tw', 'zh-hant', 'zh'),
    'zh-sg': ('zh-sg', 'zh-hans', 'zh'),
    'zh-my': ('zh-my', 'zh-sg', 'zh-hans', 'zh'),
    'zh-mo': ('zh-mo', 'zh-hk', 'zh-hant', 'zh'),
    'zh-hant': ('zh-hant', 'zh-tw', 'zh-hk', 'zh'),
    'zh-hans': ('zh-hans', 'zh-cn', 'zh-sg', 'zh')
}

DICTIONARY = "zhcdict.json"

zhcdicts = None
dict_zhcn = None
dict_zhsg = None
dict_zhtw = None
dict_zhhk = None

def require_initialized(fn):
    """
    Ensure the dict is loaded.
    Copied from Jieba.
    """
    @wraps(fn)
    def wrapped(*args, **kwargs):
        global zhcdicts
        if zhcdicts:
            return fn(*args, **kwargs)
        else:
            loaddict(DICTIONARY)
            return fn(*args, **kwargs)

    return wrapped

def loaddict(filename='zhcdict.json'):
    global zhcdicts
    if zhcdicts:
        return
    _curpath=os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    abs_path = os.path.join(_curpath, filename)
    with open(abs_path, 'r') as f:
        zhcdicts = json.load(f)

@require_initialized
def getdict(locale):
    """
    Generate or get convertion dict cache for certain locale.
    """
    global dict_zhcn, dict_zhsg, dict_zhtw, dict_zhhk
    if locale == 'zh-hans':
        return zhcdicts['zh2Hans']
    elif locale == 'zh-hant':
        return zhcdicts['zh2Hant']
    elif locale == 'zh-cn':
        if dict_zhcn:
            return dict_zhcn
        else:
            dict_zhcn = zhcdicts['zh2Hans'].copy()
            dict_zhcn.update(zhcdicts['zh2CN'])
            return dict_zhcn
    elif locale in ('zh-sg', 'zh-my'):
        if dict_zhsg:
            return dict_zhsg
        else:
            dict_zhsg = zhcdicts['zh2Hans'].copy()
            dict_zhsg.update(zhcdicts['zh2SG'])
            return dict_zhsg
    elif locale == 'zh-tw':
        if dict_zhtw:
            return dict_zhtw
        else:
            dict_zhtw = zhcdicts['zh2Hant'].copy()
            dict_zhtw.update(zhcdicts['zh2TW'])
            return dict_zhtw
    elif locale in ('zh-hk', 'zh-mo'):
        if dict_zhhk:
            return dict_zhhk
        else:
            dict_zhhk = zhcdicts['zh2Hant'].copy()
            dict_zhhk.update(zhcdicts['zh2HK'])
            return dict_zhhk

@require_initialized
def convert(s, locale):
    """
    Main convert function.
    `s` must be unicode (Python 2) or str (Python 3).
    `locale` should be one of ('zh-hans', 'zh-hant', 'zh-cn', 'zh-sg'
                               'zh-tw', 'zh-hk', 'zh-my', 'zh-mo')

    >>> print(convert(u'我幹什麼不干你事。', 'zh-cn'))
    我干什么不干你事。
    >>> print(convert(u'人体内存在很多微生物', 'zh-tw'))
    人體內存在很多微生物
    """
    zhdict = getdict(locale)
    pos = 0
    ch = []
    expr = s
    maxlen = len(max(zhdict, key=len))
    while pos < len(expr):
        flen = min(maxlen, len(expr) - pos)
        oper = None
        outword = None
        while not oper in zhdict:
            if flen < 1:
                outword = oper
                oper = None
                break
            oper = expr[pos:pos + flen]
            flen -= 1
        if oper:
            ch.append(zhdict[oper])
        elif outword:
            ch.append(outword)
        pos += flen + 1
    return ''.join(ch)

@require_initialized
def convert_for_mw(s, locale):
    """
    Recognizes MediaWiki's human conversion format.

    >>> print(convert_for_mw(u'在现代，机械计算-{}-机的应用已经完全被电子计算-{}-机所取代', 'zh-hk'))
    在現代，機械計算機的應用已經完全被電子計算機所取代
    >>> print(convert_for_mw(u'-{zh-hant:資訊工程;zh-hans:计算机工程学;}-是电子工程的一个分支，主要研究计算机软硬件和二者间的彼此联系。', 'zh-tw'))
    資訊工程是電子工程的一個分支，主要研究計算機軟硬體和二者間的彼此聯繫。
    >>> print(convert_for_mw(u'張國榮曾在英國-{zh:利兹;zh-hans:利兹;zh-hk:列斯;zh-tw:里茲}-大学學習。', 'zh-hant'))
    張國榮曾在英國里茲大學學習。
    >>> print(convert_for_mw(u'張國榮曾在英國-{zh:利兹;zh-hans:利兹;zh-hk:列斯;zh-tw:里茲}-大学學習。', 'zh-sg'))
    张国荣曾在英国利兹大学学习。
    """
    zhdict = getdict(locale)
    pos = 0
    ch = []
    expr = s
    maxlen = len(max(zhdict, key=len))
    while pos < len(expr):
        flen = min(maxlen, len(expr) - pos)
        oper = None
        outword = None
        while not oper in zhdict:
            if flen < 1:
                outword = oper
                oper = None
                break
            oper = expr[pos:pos + flen]
            if flen == 2 and oper == '-{':
                endwith = expr.find('}-', pos + flen)
                brace = expr[pos + flen:endwith]
                if not brace.strip():
                    flen = 3
                    oper = None
                    outword = ''
                    break
                manconv = brace.strip().split(';')
                if len(manconv) == 1:
                    outword = manconv[0].split(':')[-1].strip()
                    flen = len(outword) + 3
                else:
                    regd = {}
                    for i in manconv:
                        it = i.strip()
                        if not it:
                            continue
                        reglist = it.split(':')
                        regd[reglist[0].strip()] = reglist[1].strip()
                    for lc in locales.get(locale, ()):
                        if lc in regd:
                            outword = regd[lc]
                            break
                    else:
                        outword = regd.popitem()[1]
                    flen = len(brace) + 3
                oper = None
                break
            flen -= 1
        if oper:
            ch.append(zhdict[oper])
        elif outword:
            ch.append(outword)
        pos += flen + 1
    return ''.join(ch)

def main():
    """
    Simple stdin/stdout interface.
    """
    if len(sys.argv) < 2:
        print("usage: %s {zh-cn|zh-tw|zh-hk|zh-sg|zh-hans|zh-hant}" % __file__)
        sys.exit()
    loaddict()
    ln = sys.stdin.readline()
    while ln:
        l = ln.rstrip('\r\n')
        if sys.version_info[0] < 3:
            l = unicode(l, 'utf-8')
        print(convert_for_mw(l, sys.argv[1]))
        ln = sys.stdin.readline()

if __name__ == '__main__':
    main()
