import unittest

import interface
from Zasady import Zasady_podstawowe


class Testy(unittest.TestCase):
    def test1(self):
        gra = interface.gra
        canvas = interface.canvas

        gra.restart()

        gra.klikniecie(1)
        gra.klikniecie(1)
        gra.klikniecie(1)
        gra.klikniecie(1)

        self.assertEqual(Zasady_podstawowe.znajdz_w_liscie_stat(canvas, gra.pola, 6, 1), "red")
        self.assertEqual(Zasady_podstawowe.znajdz_w_liscie_stat(canvas, gra.pola, 5, 1), "yellow")
        self.assertEqual(Zasady_podstawowe.znajdz_w_liscie_stat(canvas, gra.pola, 4, 1), "red")
        self.assertEqual(Zasady_podstawowe.znajdz_w_liscie_stat(canvas, gra.pola, 3, 1), "yellow")

    def test2(self):
        gra = interface.gra

        gra.restart()

        gra.klikniecie(1)
        gra.klikniecie(2)
        gra.klikniecie(1)
        gra.klikniecie(2)
        gra.klikniecie(1)
        gra.klikniecie(2)
        wynik = gra.klikniecie(1)

        self.assertEqual(wynik, 1)

    def test3(self):
        gra = interface.gra

        gra.restart()

        gra.klikniecie(1)
        gra.klikniecie(2)

        gra.klikniecie(2)
        gra.klikniecie(3)


        gra.klikniecie(3)
        gra.klikniecie(4)

        gra.klikniecie(4)
        wynik = gra.klikniecie(5)

        self.assertEqual(wynik, 2)

    def test4(self):
        gra = interface.gra

        gra.restart()

        gra.klikniecie(1)
        gra.klikniecie(2)

        gra.klikniecie(2)
        gra.klikniecie(3)

        gra.klikniecie(3)
        gra.klikniecie(4)

        gra.klikniecie(3)
        gra.klikniecie(4)

        gra.klikniecie(5)
        gra.klikniecie(4)
        wynik = gra.klikniecie(4)

        self.assertEqual(wynik, 1)

    def test5(self):
        gra = interface.gra

        gra.restart()

        gra.klikniecie(1)
        gra.klikniecie(2)
        gra.klikniecie(1)
        gra.klikniecie(2)
        gra.klikniecie(1)
        gra.klikniecie(2)

        gra.klikniecie(2)
        gra.klikniecie(1)
        gra.klikniecie(2)
        gra.klikniecie(1)
        gra.klikniecie(2)
        gra.klikniecie(1)


        gra.klikniecie(3)
        gra.klikniecie(4)
        gra.klikniecie(3)
        gra.klikniecie(4)
        gra.klikniecie(3)
        gra.klikniecie(4)

        gra.klikniecie(4)
        gra.klikniecie(3)
        gra.klikniecie(4)
        gra.klikniecie(3)
        gra.klikniecie(4)
        gra.klikniecie(3)


        gra.klikniecie(5)
        gra.klikniecie(6)
        gra.klikniecie(5)
        gra.klikniecie(6)
        gra.klikniecie(5)
        gra.klikniecie(6)

        gra.klikniecie(6)
        gra.klikniecie(5)
        gra.klikniecie(6)
        gra.klikniecie(5)
        gra.klikniecie(6)
        gra.klikniecie(5)


        gra.klikniecie(7)
        gra.klikniecie(7)
        gra.klikniecie(7)
        gra.klikniecie(7)
        gra.klikniecie(7)
        wynik = gra.klikniecie(7)

        self.assertEqual(wynik, 0)

    def test6(self):
        gra = interface.gra

        gra.restart()

        gra.klikniecie(1)
        gra.klikniecie(1)
        gra.klikniecie(2)
        gra.klikniecie(2)
        gra.klikniecie(3)
        gra.klikniecie(3)
        gra.klikniecie(5)
        gra.klikniecie(5)
        gra.klikniecie(6)
        gra.klikniecie(6)
        gra.klikniecie(7)
        gra.klikniecie(7)
        wynik = gra.klikniecie(4)

        self.assertEqual(wynik, 1)

    def test7(self):
        gra = interface.gra

        gra.restart()

        gra.klikniecie(1)
        gra.klikniecie(1)
        gra.klikniecie(1)
        gra.klikniecie(1)
        gra.klikniecie(1)
        gra.klikniecie(1)
        with self.assertRaises(Exception):
            gra.klikniecie(1)
