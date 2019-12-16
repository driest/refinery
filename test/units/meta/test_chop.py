#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .. import TestUnitBase


class TestChop(TestUnitBase):

    def test_check_invalid_args(self):
        for k in ('"-200000000"', '"-10"', 0, B'FOOBAR'):
            with self.assertRaises(Exception):
                self.load(k)

    def test_simple_chunk_with_custom_separator(self):
        for n in range(1, 20):
            unit = self.load(n)
            for m in range(1, 20):
                self.assertEqual(
                    unit(B'A' * n * m),
                    B'\n'.join([B'A' * n for _ in range(m)])
                )

    def test_uneven_chop(self):
        unit = self.load(3)
        self.assertEqual(unit(B'ABCDEFGH'), B'ABC\nDEF\nGH')