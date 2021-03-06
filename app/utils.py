# -*- coding: utf-8 -*- 
__author__ = 'ivany'


def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

def filterHtml(html):
    import re
    dr = re.compile(r'<[^>]+>', re.S)
    return dr.sub('', html)