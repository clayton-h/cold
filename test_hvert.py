import unittest
from hvert import nearest
from hvert import global_cities


class Testhvert(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mulating'
        ans = nearest(city, global_cities)
        expected = 'Akureyri'
        self.assertEqual(ans, expected)


class Testhvert2(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mosfellsbaer'
        ans = nearest(city, global_cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class Testhvert3(unittest.TestCase):
    def test1(self) -> None:
        city = 'Reykjavik'
        ans = nearest(city, global_cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class Testhvert4(unittest.TestCase):
    def test1(self) -> None:
        city = 'Akureyri'
        ans = nearest(city, global_cities)
        expected = 'Akureyri'
        self.assertEqual(ans, expected)


class Testhvert5(unittest.TestCase):
    def test1(self) -> None:
        city = 'Kopavogur'
        ans = nearest(city, global_cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)


class Testhvert6(unittest.TestCase):
    def test1(self) -> None:
        city = 'Mosfellsbaer'
        ans = nearest(city, global_cities)
        expected = 'Reykjavik'
        self.assertEqual(ans, expected)
