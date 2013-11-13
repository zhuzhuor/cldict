#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from cldict import dictcn


class TestDict(unittest.TestCase):
    def test_lookup(self):
        result = dictcn.look_up('test')
        self.assertIn('word', result)
        self.assertIn('test', result['word'])
        self.assertIn('phonetic', result)
        self.assertIn('[test]', result['phonetic'])
        self.assertIn('explanation', result)
        self.assertIn(u'测试', result['explanation'])


if __name__ == '__main__':
    unittest.main()
