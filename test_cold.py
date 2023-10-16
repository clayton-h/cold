import unittest
from cold import findCloserCity
from cold import cities


class TestCold(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mulating'
        ans = findCloserCity(city, cities)
        expected = 'Akureyri'
        self.assertEqual(ans, expected)


class TestCold(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mosfellsbaer'
        ans = findCloserCity(city, cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class TestCold(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mulating'
        ans = findCloserCity(city, cities)
        expected = 'Akureyri'
        self.assertEqual(ans, expected)
