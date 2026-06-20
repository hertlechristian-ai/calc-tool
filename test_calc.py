"""Tests für das Taschenrechner-Modul (mit dem eingebauten unittest)."""

import unittest

from calc import add, multiply, subtract


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 99), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 6), 4)
        self.assertEqual(subtract(0, 5), -5)


if __name__ == "__main__":
    unittest.main()
