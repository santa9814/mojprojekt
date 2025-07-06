import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import kalkulator

class TestKalkulator(unittest.TestCase):
    def test_dodawanie(self):
        self.assertEqual(kalkulator.dodaj(2, 3), 5)

    def test_odejmowanie(self):
        self.assertEqual(kalkulator.odejmij(5, 3), 2)

    def test_mnozenie(self):
        self.assertEqual(kalkulator.pomnoz(4, 2), 8)

    def test_dzielenie(self):
        self.assertEqual(kalkulator.podziel(10, 2), 5.0)

    def test_dzielenie_przez_zero(self):
        with self.assertRaises(ValueError):
            kalkulator.podziel(1, 0)
