#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Combines TAB seperated dictionaries (OpenCC text format) into zhcdict.json
Ignores lines with multiple values.

Usage: combinedict.py STCharacters.txt {zh2Hans|zh2Hant|zh2CN|zh2HK|zh2SG|zh2TW}=filename ...

Example:

combinedict.py STCharacters.txt zh2Hans=TSCharacters.txt zh2Hant=STCharacters.txt zh2HK=HKVariants.txt zh2TW=TWVariants.txt

Don't combine the phrase tables, the result will be unexpected.
"""

import sys
import json

DICTS = frozenset(('zh2Hans', 'zh2Hant', 'zh2CN', 'zh2HK', 'zh2SG', 'zh2TW'))

def main():
    if len(sys.argv) > 2:
        files = sys.argv[2:]
    else:
        print(__doc__)
        sys.exit(1)

    norm_dict = {}
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        for ln in f:
            k, v = ln.strip().split('\t', 1)
            for norm_ch in v.split():
                norm_dict[norm_ch] = k

    je = json.JSONEncoder(ensure_ascii=False, indent=0, separators=(',', ': '), sort_keys=True)
    zhdict = json.load(open('zhcdict.json', 'r'))
    SIMPONLY, TRADONLY = set(), set()
    for dic in files:
        target, filename = dic.split('=')
        assert target in DICTS
        with open(filename, 'rb') as f:
            for ln in f:
                k, v = ln.strip().decode('utf-8').split('\t')
                first_v = v.split(' ')[0]
                if k != first_v:
                    zhdict[target][k] = first_v
                norm_k = norm_dict.get(k, k)
                if norm_k != k and k != first_v:
                    zhdict[target][norm_k] = first_v
                if target == 'zh2Hans':
                    TRADONLY.add(k)
                elif target == 'zh2Hant':
                    SIMPONLY.add(k)
    overlapped = SIMPONLY.intersection(TRADONLY)
    zhdict['SIMPONLY'] = ''.join(sorted(SIMPONLY.difference(overlapped)))
    zhdict['TRADONLY'] = ''.join(sorted(TRADONLY.difference(overlapped)))
    for target in DICTS.difference(zhdict.keys()):
        zhdict[target] = {}
    with open('zhcdict.json', 'wb') as f:
        for chunk in je.iterencode(zhdict):
            f.write(chunk.encode('utf-8'))
        f.write(b'\n')

if __name__ == '__main__':
    main()
