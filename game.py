from operator import itemgetter
from tkinter.constants import DISABLED, NORMAL

import interface
from GameUser import gracz
from Zasady import zasady_pion_poziom


class gra:
    def __init__(self, canvas):
        self.pola = list()
        self.canvas = canvas
        self.gracz1 = gracz(1, "red")
        self.gracz2 = gracz(2, 'yellow')
        self.tura_gracza = self.gracz1
        self.zasady_pion_poziom = zasady_pion_poziom(self.canvas)

    def znajdz_pole(self, numer):
        pola_w_kolumnie = [(p, w) for (p, w, k) in self.pola if
                           k == numer and self.canvas.itemcget(p, 'fill') != 'red' and self.canvas.itemcget(p,
                                                                                                            'fill') != 'yellow']
        if pola_w_kolumnie == []:
            return None
        if len(pola_w_kolumnie) == 1:
            interface.przycisk_kolumna[numer]["state"] = DISABLED
        return max(pola_w_kolumnie, key=itemgetter(1))[0]

    def klikniecie(self, numer):
        # interface.button["state"] = DISABLED
        # 1. Pobierasz najnizsza kulke
        # 2. Ustawiasz jej kolor
        # 3. Sprawdzasz ktowygral() - > jeżęli wygrał to blokuejsz całą gre i wyświetlasz kto wygrał
        # 4. Zmienaisz aktywnego gracza (jezeli gra jesszce trwa)
        # 5.  Jeżeli kliekniety wietsz == 1 to blokuje przycisk
        pole_do_wypelnienia = self.znajdz_pole(numer)
        if pole_do_wypelnienia is None:
            return
        self.canvas.itemconfig(pole_do_wypelnienia, fill=self.tura_gracza.kolor)
        self.zmiana_tury()
        wynik = self.zasady_pion_poziom.Kto_wygrał(self.pola)
        if wynik == 1 or wynik == 2:
            print("Wygral gracz {}".format(wynik))

    def restart(self):
        for przycisk in self.pola:
            self.canvas.itemconfig(przycisk[0], fill="")
        self.tura_gracza = self.gracz1
        interface.gracz.set("Tura gracza {}".format(self.tura_gracza.id))
        for i in range(1, len(interface.przycisk_kolumna) + 1):
            interface.przycisk_kolumna[i]["state"] = NORMAL

    def zmiana_tury(self):
        if self.tura_gracza == self.gracz1:
            self.tura_gracza = self.gracz2
        else:
            self.tura_gracza = self.gracz1
        interface.gracz.set("Tura gracza {}".format(self.tura_gracza.id))
