import unittest
from hvert import findCloserCity
from hvert import cities


class Testhvert(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mulating'
        ans = findCloserCity(city, cities)
        expected = 'Akureyri'
        self.assertEqual(ans, expected)


class Testhvert2(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mosfellsbaer'
        ans = findCloserCity(city, cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class Testhvert3(unittest.TestCase):
    def test1(self) -> None:
        city = 'Reykjavik'
        ans = findCloserCity(city, cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class Testhvert4(unittest.TestCase):
    def test1(self) -> None:
        city = 'Akureyri'
        ans = findCloserCity(city, cities)
        expected = 'Akureyri'
        self.assertEqual(ans, expected)


class Testhvert5(unittest.TestCase):
    def test1(self) -> None:
        city = 'Kopavogur'
        ans = findCloserCity(city, cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class Testhvert6(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mosfellsbaer'
        ans = findCloserCity(city, cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)
