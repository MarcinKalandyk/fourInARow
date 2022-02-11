from operator import itemgetter
from tkinter.constants import DISABLED, NORMAL

import interface
from GameUser import gracz
from Zasady import zasady_pion_poziom, zasady_skos


class gra:
    def __init__(self, canvas):
        """

        :param canvas: edytowalne pole w którym mogą znajdować się napisy, rysunki itd
        """
        self.pola = list()
        self.canvas = canvas
        self.gracz1 = gracz(1, "red")
        self.gracz2 = gracz(2, 'yellow')
        self.tura_gracza = self.gracz1
        self.zasady_pion_poziom = zasady_pion_poziom(self.canvas)
        self.zasady_skos = zasady_skos(self.canvas)

    def znajdz_pole(self, numer):
        """

        :param numer: numer kolumny
        :return: zwraca najniższe (o najwyższym indeksie)  nie zapełnione pole w kolumnie
        """
        pola_w_kolumnie = [(p, w) for (p, w, k) in self.pola if
                           k == numer and self.canvas.itemcget(p, 'fill') != 'red' and self.canvas.itemcget(p,
                                                                                                            'fill') != 'yellow']
        if pola_w_kolumnie == []:
            return None
        if len(pola_w_kolumnie) == 1:
            interface.przycisk_kolumna[numer]["state"] = DISABLED
        return max(pola_w_kolumnie, key=itemgetter(1))[0]

    def klikniecie(self, numer):
        """
        obsługa kliknięcia, zapełnia pole jeśli nie zapełnione, zmienia ture, wywołuje sprawdzenie warunków zwycięstwa.
        :param numer: numer kolumny
        :return: zwraca wynik (zwyciężce) jeśli wystąpiły warunki zwycięśtwa, zwraca 0 jeśli remis
        """
        pole_do_wypelnienia = self.znajdz_pole(numer)
        if pole_do_wypelnienia is None:
            raise Exception("Pola w tej kolumnie zostaly juz zapelnione")
        self.canvas.itemconfig(pole_do_wypelnienia, fill=self.tura_gracza.kolor)
        self.zmiana_tury()

        wynik = self.zasady_pion_poziom.Kto_wygrał(self.pola)
        if wynik == 1 or wynik == 2:
            self.zakoncz_gre(wynik)
            return wynik
        wynik = self.zasady_skos.Kto_wygrał(self.pola)
        if wynik == 1 or wynik == 2:
            self.zakoncz_gre(wynik)
            return wynik
        if self.czy_remis():
            self.zakoncz_gre(None)
            return 0

    def czy_remis(self):
        """

        :return: zwraca status (zbiorowy ) zablokowania przycisków wszystkie zablokowane /nie wsyztskie zablokowane
        """
        for p in range(1, 8):
            if interface.przycisk_kolumna[p]["state"] == NORMAL:
                return False
        return True

    def restart(self):
        """
        czyści pole gry, odblokowuje wszystkie przyciski, ustawia turę gracza na turę gracza 1
        :return:
        """
        for przycisk in self.pola:
            self.canvas.itemconfig(przycisk[0], fill="")
        self.tura_gracza = self.gracz1
        interface.gracz.set("Tura gracza {}".format(self.tura_gracza.id))
        for i in range(1, len(interface.przycisk_kolumna) + 1):
            interface.przycisk_kolumna[i]["state"] = NORMAL

    def zmiana_tury(self):
        """
        zmienia turę gracza na przeciwną
        :return:
        """
        if self.tura_gracza == self.gracz1:
            self.tura_gracza = self.gracz2
        else:
            self.tura_gracza = self.gracz1
        interface.gracz.set("Tura gracza {}".format(self.tura_gracza.id))

    def zakoncz_gre(self, wynik):
        """
        metoda wywołująca okno do wyświetlenia wyniku gry oraz blokująca kolumny (przyciski)
        :param wynik: zwraca id zwyciężcy
        :return:
        """
        for p in range(1, 8):
            interface.przycisk_kolumna[p]["state"] = DISABLED
        if wynik is not None:
            interface.okno_koniec_gry("Wygral gracz {}".format(wynik))
        else:
            interface.okno_koniec_gry("Remis")
