"""Tests für das Taschenrechner-Modul (mit dem eingebauten unittest)."""

import unittest

from calc import add, multiply


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 99), 0)

    # Hinweis: Für subtract() fehlt noch ein Test – das holen wir im ersten PR nach.


if __name__ == "__main__":
    unittest.main()
