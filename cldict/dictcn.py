#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from urllib import urlencode


def look_up(phrase=None):
    if phrase is None:
        return

    resp = requests.get('http://3g.dict.cn/s.php?' +
                        urlencode({'q': phrase.encode('utf-8')}))
    resp.encoding = 'UTF-8'
    # soup = BeautifulSoup(resp.text, 'lxml')
    soup = BeautifulSoup(resp.text)

    info = {}

    phrase = soup.find('h1')
    if phrase:
        info['phrase'] = phrase.get_text().strip()

    phonetic = soup.find('div', class_='phonetic')
    if phonetic:
        for p in phonetic.contents:
            p_text = unicode(p)
            if u'美' in p_text:
                if '<bdo>' in p_text:
                    info['phonetic'] = p.bdo.get_text().strip()
                if 'audioPlay(this)' in p_text:
                    info['audio'] = \
                        'http://audio.dict.cn/output.php?id=' + p.i['audio']
                break
        if 'phonetic' not in info:
            p = phonetic.contents[0]
            p_text = unicode(p)
            if '<bdo>' in p_text:
                info['phonetic'] = p.bdo.get_text().strip()
            if 'audioPlay(this)' in p_text:
                info['audio'] = \
                    'http://audio.dict.cn/output.php?id=' + p.i['audio']

    explanation = soup.find('div', class_='exp')
    if explanation:
        info['explanation'] = explanation.get_text().strip()

    transform = soup.find('p', class_='transformc')
    if transform:
        info['transform'] = transform.get_text().strip()

    return info


if __name__ == '__main__':
    result = look_up('take')
    for i in result:
        print i.upper()
        print result[i]
    print

    result = look_up('good morning')
    for i in result:
        print i.upper()
        print result[i]
    print

    result = look_up(u'试试')
    for i in result:
        print i.upper()
        print result[i]
    print

    result = look_up('123')
    for i in result:
        print i.upper()
        print result[i]
    print
