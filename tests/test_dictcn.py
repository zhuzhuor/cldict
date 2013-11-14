#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from cldict import dictcn


class TestDict(unittest.TestCase):
    def test_lookup_word(self):
        result = dictcn.look_up('test')
        self.assertIn('phrase', result)
        self.assertEqual('test', result['phrase'])
        self.assertIn('phonetic', result)
        self.assertEqual('[test]', result['phonetic'])
        self.assertIn('explanation', result)
        self.assertIn(u'测试', result['explanation'])

    def test_lookup_phrase(self):
        result = dictcn.look_up('good morning')
        self.assertIn('phrase', result)
        self.assertEqual('good morning', result['phrase'])
        self.assertIn('explanation', result)
        self.assertEqual(u'早上好', result['explanation'])

    def test_lookup_numbers(self):
        result = dictcn.look_up('123')
        self.assertIn('phrase', result)
        self.assertEqual('123', result['phrase'])
        self.assertIn('explanation', result)
        self.assertIn('one hundred and twenty three', result['explanation'])

    def test_lookup_chinese(self):
        result = dictcn.look_up(u'试试')
        self.assertIn('phrase', result)
        self.assertEqual(u'试试', result['phrase'])


if __name__ == '__main__':
    unittest.main()
