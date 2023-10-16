import unittest
from cold import findCloserCity
from cold import cities


class TestCold(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mulating'
        ans = findCloserCity(city, cities)
        expected = 'Akureyri'
        self.assertEqual(ans, expected)


class TestCold2(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mosfellsbaer'
        ans = findCloserCity(city, cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class TestCold3(unittest.TestCase):
    def test1(self) -> None:
        city = 'Reykjavik'
        ans = findCloserCity(city, cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class TestCold4(unittest.TestCase):
    def test1(self) -> None:
        city = 'Akureyri'
        ans = findCloserCity(city, cities)
        expected = 'Akureyri'
        self.assertEqual(ans, expected)


class TestCold5(unittest.TestCase):
    def test1(self) -> None:
        city = 'Kopavogur'
        ans = findCloserCity(city, cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class TestCold6(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mosfellsbaer'
        ans = findCloserCity(city, cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)
