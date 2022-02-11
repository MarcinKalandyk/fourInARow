import numpy


class Zasady_podstawowe:
    kolumny = 7
    wiersze = 6

    def __init__(self, canvas):
        """
        Tworzy obiekt zasad przyjmujący siebie i canvas dzięki niej wsyzstkie dziedziczące zasady mają ten sam konstruktor
        :param canvas: edytowalne pole w którym mogą znajdować się napisy, rysunki itd
        """
        self.canvas = canvas

    def Kto_wygrał(self, lista_pol):
        """
        metoda virtualana zwracająca informacje o wygranej
        :param lista_pol: lista zawierająca tuple z przyciskiem i wsółrzędnymi
        :return:
        """
        pass

    def znajdz_w_liscie(self, lista_pol, wiersz, kolumna):
        """
        p - przechowuje kolor
        w -numer wiersza
        k - numer kolumny
        :param lista_pol: lista zawierająca tuple z przyciskiem i wsółrzędnymi
        :param wiersz: numer współrzędnej  wiersza
        :param kolumna: numer współrzędnej  kolumny
        :return: zwraca pole o podanych współrzędnych
        """
        return self.canvas.itemcget([p for (p, w, k) in lista_pol if w == wiersz and k == kolumna][0], 'fill')

    @staticmethod
    def znajdz_w_liscie_stat(canvas, lista_pol, wiersz, kolumna):
        """
        metoda statyczne (pomocnicza dla testów)
        :param canvas: edytowalne pole w którym mogą znajdować się napisy, rysunki itd
        :param lista_pol: lista zawierająca tuple z przyciskiem i wsółrzędnymi
        :param wiersz: numer współrzędnej  wiersza
        :param kolumna: numer współrzędnej  kolumny
        :return: zwraca pole o podanych współrzędnych
        """
        return canvas.itemcget([p for (p, w, k) in lista_pol if w == wiersz and k == kolumna][0], 'fill')



class zasady_pion_poziom(Zasady_podstawowe):

    def Kto_wygrał(self, lista_pol):
        """
        Sprawdzanie zwyciężcy pionowo i poziomo
        :param lista_pol: lista zawierająca tuple z przyciskiem i wsółrzędnymi
        :return: id zwycięskiego gracza lub none jeśli nikt nie wygrał
        """

        gracz_1_pionowo = self.sprawdz_pionowo(lista_pol, "red")
        gracz_2_pionowo = self.sprawdz_pionowo(lista_pol, "yellow")
        gracz_1_poziomo = self.sprawdz_poziomo(lista_pol, "red")
        gracz_2_poziomo = self.sprawdz_poziomo(lista_pol, "yellow")
        if gracz_1_poziomo or gracz_1_pionowo:
            return 1
        if gracz_2_poziomo or gracz_2_pionowo:
            return 2
        return None

    def sprawdz_poziomo(self, lista_pol, kolor):
        """
        metoda do sprawdzenia zwyciężcy pozuiomo
        :param lista_pol: lista zawierająca tuple z przyciskiem i wsółrzędnymi
        :param kolor: kolor pola
        :return: zwraca true jeżeli znalazło zwyciężce poziomo
        """
        for c in range(1, self.kolumny - 2):
            for r in range(1, self.wiersze + 1):
                if self.znajdz_w_liscie(lista_pol, r, c) == kolor and self.znajdz_w_liscie(lista_pol, r,
                                                                                           c + 1) == kolor and self.znajdz_w_liscie(
                    lista_pol, r, c + 2) == kolor and self.znajdz_w_liscie(lista_pol, r, c + 3) == kolor:
                    return True

    def sprawdz_pionowo(self, lista_pol, kolor):
        """
        metoda do sprawdzenia zwyciężcy pionowo
        :param lista_pol: lista zawierająca tuple z przyciskiem i wsółrzędnymi
        :param kolor: kolor pola
        :return: zwraca true jeżeli znalazło zwyciężce pionowo
        """
        for c in range(1, self.kolumny + 1):
            for r in range(1, self.wiersze - 2):
                if self.znajdz_w_liscie(lista_pol, r, c) == kolor and self.znajdz_w_liscie(lista_pol, r + 1,
                                                                                           c) == kolor and self.znajdz_w_liscie(
                    lista_pol, r + 2, c) == kolor and self.znajdz_w_liscie(lista_pol, r + 3, c) == kolor:
                    return True


class zasady_skos(Zasady_podstawowe):

    def Kto_wygrał(self, lista_pol):
        """
        Sprawdzanie zwyciężcy po skosach
        :param lista_pol: lista zawierająca tuple z przyciskiem i wsółrzędnymi
        :return: id zwycięskiego gracza lub none jeśli nikt nie wygrał
        """

        gracz_1_skos_gore = self.skos_w_gore(lista_pol, "red")
        gracz_2_skos_gore = self.skos_w_gore(lista_pol, "yellow")
        gracz_1_skos_dol = self.skos_w_dol(lista_pol, "red")
        gracz_2_skos_dol = self.skos_w_dol(lista_pol, "yellow")
        if (gracz_1_skos_dol or gracz_1_skos_gore):
            return 1
        if (gracz_2_skos_dol or gracz_2_skos_gore):
            return 2
        return None

    def skos_w_dol(self, lista_pol, kolor):
        """
        metoda do sprawdzenia zwyciężcy w opadającym skosie
        :param lista_pol: lista zawierająca tuple z przyciskiem i wsółrzędnymi
        :param kolor: kolor pola
        :return:  zwraca true jeżeli znalazło zwyciężce w opadającym skosie
        """
        for c in range(1, self.kolumny - 2):
            for r in range(1, self.wiersze - 2):
                if self.znajdz_w_liscie(lista_pol, r, c) == kolor and self.znajdz_w_liscie(lista_pol, r + 1,
                                                                                           c + 1) == kolor and self.znajdz_w_liscie(
                    lista_pol, r + 2, c + 2) == kolor and self.znajdz_w_liscie(lista_pol, r + 3, c + 3) == kolor:
                    return True

    def skos_w_gore(self, lista_pol, kolor):
        """
        metoda do sprawdzenia zwyciężcy w rosnącym skosie
        :param lista_pol: lista zawierająca tuple z przyciskiem i wsółrzędnymi
        :param kolor: kolor pola
        :return: zwraca true jeżeli znalazło zwyciężce w rosnącym skosie
        """
        for c in range(1, self.kolumny - 2):
            for r in range(4, self.wiersze + 1):
                if self.znajdz_w_liscie(lista_pol, r, c) == kolor and self.znajdz_w_liscie(lista_pol, r - 1,
                                                                                           c + 1) == kolor and self.znajdz_w_liscie(
                    lista_pol, r - 2, c + 2) == kolor and self.znajdz_w_liscie(lista_pol, r - 3, c + 3) == kolor:
                    return True
