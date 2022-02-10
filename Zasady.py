import numpy


class Zasady_podstawowe:
    kolumny = 7
    wiersze = 6

    def Kto_wygrał(self, lista_pol):
        pass

    def znajdz_w_liscie(self, lista_pol, wiersz, kolumna):
        return self.canvas.itemcget([p for (p, w, k) in lista_pol if w == wiersz and k == kolumna][0], 'fill')

    def __init__(self, canvas):
        self.canvas = canvas


class zasady_pion_poziom(Zasady_podstawowe):

    def Kto_wygrał(self, lista_pol):
        # warunek poziomy

        gracz_1_poziomo= self.sprawdz_poziomo(lista_pol,"red")
        gracz_2_poziomo= self.sprawdz_poziomo(lista_pol,"yellow")
        if gracz_1_poziomo:
            return 1
        if gracz_2_poziomo:
            return 2
        return None

    def sprawdz_poziomo(self, lista_pol, kolor):
        for c in range(1,self.kolumny - 2):
            for r in range(1,self.wiersze+1):
                if self.znajdz_w_liscie(lista_pol, r, c) == kolor and self.znajdz_w_liscie(lista_pol, r,
                                                                                           c + 1) == kolor and self.znajdz_w_liscie(
                        lista_pol, r, c + 2) == kolor and self.znajdz_w_liscie(lista_pol, r, c + 3) == kolor:
                    return True

        # Check vertical locations for win
"""
 for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

        # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                    board[r + 3][c + 3] == piece:
                return True

        # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                    board[r - 3][c + 3] == piece:
                return True
"""