import unittest
from hvert import find_closer_city
from hvert import global_cities


class Testhvert(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mulating'
        ans = find_closer_city(city, global_cities)
        expected = 'Akureyri'
        self.assertEqual(ans, expected)


class Testhvert2(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mosfellsbaer'
        ans = find_closer_city(city, global_cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class Testhvert3(unittest.TestCase):
    def test1(self) -> None:
        city = 'Reykjavik'
        ans = find_closer_city(city, global_cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class Testhvert4(unittest.TestCase):
    def test1(self) -> None:
        city = 'Akureyri'
        ans = find_closer_city(city, global_cities)
        expected = 'Akureyri'
        self.assertEqual(ans, expected)


class Testhvert5(unittest.TestCase):
    def test1(self) -> None:
        city = 'Kopavogur'
        ans = find_closer_city(city, global_cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class Testhvert6(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mosfellsbaer'
        ans = find_closer_city(city, global_cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)
