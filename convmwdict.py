#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import json

PHPHEAD = re.compile(r'<\?php.+?/\*.+?\*/', re.DOTALL)
VARS = re.compile(r'\$(\w+?) = array\(\s+(.+?)\s+\);', re.DOTALL)

def convert(phpfile):
    f = PHPHEAD.sub('', phpfile)
    matches = VARS.findall(f)
    zhcdict = {}
    for i in matches:
        groups = i[1].rstrip(',').split(',')
        zhcdict[i[0]] = dict(
            ((w.strip("' ") for w in g.strip().split('=>')) for g in groups))
    return zhcdict


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'ZhConversion.php'
    with open(filename, 'r') as f:
        phpfile = f.read()
    if sys.version_info[0] < 3:
        phpfile = unicode(phpfile, 'utf-8')
    je = json.JSONEncoder(ensure_ascii=False, indent=0, separators=(',', ': '), sort_keys=True)
    with open('zhcdict.json', 'wb') as f:
        for chunk in je.iterencode(convert(phpfile)):
            f.write(chunk.encode('utf-8'))

if __name__ == '__main__':
    main()
