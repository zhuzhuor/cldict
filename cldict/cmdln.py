#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from dictcn import look_up
from bisheng import add_spaces


def main_func():
    if len(sys.argv) < 2:
        if '.py' in sys.argv[0]:
            print 'Usage: python %s WORD' % sys.argv[0]
        else:
            print 'Usage: cldict WORD'
        print 'Look up the WORD from online dictionary'
        return

    word = sys.argv[1]
    info = look_up(word)

    print info['word'],
    if 'phonetic' in info:
        print info['phonetic']
    else:
        print
    if 'explanation' in info:
        print add_spaces(info['explanation'])
    if 'transform' in info:
        print add_spaces(info['transform'])


if __name__ == '__main__':
    main_func()
