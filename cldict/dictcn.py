#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def look_up(word=None):
    if word is None:
        return

    resp = requests.get('http://3g.dict.cn/s.php?q=' + word)
    resp.encoding = 'UTF-8'
    # soup = BeautifulSoup(resp.text, 'lxml')
    soup = BeautifulSoup(resp.text)

    info = {}

    word = soup.find('h1')
    if word:
        info['word'] = word.get_text().strip()

    phonetic = soup.find('div', class_='phonetic')
    if phonetic:
        for p in phonetic.contents:
            if u'美 <bdo>' in unicode(p):
                info['phonetic'] = p.bdo.get_text().strip()
                if 'audioPlay(this)' in unicode(p):
                    info['audio'] = \
                        'http://audio.dict.cn/output.php?id=' + p.i['audio']
                break
        if 'phonetic' not in info:
            if '<bdo>' in unicode(phonetic.contents[0]):
                info['phonetic'] = phonetic.contents[0].bdo.get_text().strip()

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
    result = look_up(u'试试')
    for i in result:
        print i.upper()
        print result[i]
