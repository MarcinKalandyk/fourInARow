import tkinter
from tkinter.constants import DISABLED

import game


def utworz_kolko(canv, x, y, r):
    """
    Eysowanie koła
    :param canv: pole do tworzenia na nim obiektu w tym porzypadku na tym polu narysowane jest koło
    :param x: Wspolrzedna x
    :param y: Wspolrzedna y
    :param r: srednica
    :return: id kolka
    """
    return canv.create_oval(x - r, y - r, x + r, y + r)


def okno_koniec_gry(wynik_gry):
    """

    :param wynik_gry: zwyciężca przekazywany w postaci string + parametr
    :return: tworzy pop-up okno informujące o wygranym
    """
    x = 75
    y = 15
    popup = tkinter.Toplevel()
    popup.geometry("250x200")
    game_over_label = tkinter.Label(popup, text="Koniec")
    game_over_label.pack(fill='x', padx=x, pady=y)

    result_label = tkinter.Label(popup, text=wynik_gry)
    result_label.pack(fill='x', padx=x, pady=y)

    close_button = tkinter.Button(popup, text="Ok", command=popup.destroy)
    close_button.pack(padx=x, pady=y)


window_height = 800
window_width = 800

window = tkinter.Tk()
window.title("Cztery w rzedzie")
window.geometry("{}x{}".format(window_width, window_height))
canvas = tkinter.Canvas(window, width=window_width, height=window_height, bg="light blue")
canvas.grid()

gra = game.gra(canvas)

gracz = tkinter.StringVar()
gracz.set("Tura gracza 1")

Text = tkinter.Text(window, height=5, width=52)
tura = tkinter.Label(window, textvariable=gracz)
tura.config(font=("Courier", 14))
Text.place()
tura.place(x=230, y=10)
x = 100
y = 70
r = 20
for i in range(0, 6):
    y += 60
    x = 100
    for j in range(0, 7):
        gra.pola.append(((utworz_kolko(canvas, x, y, r)), i + 1, j + 1))
        x += 60

button = tkinter.Button(window, text="Kol 1", command=lambda: gra.klikniecie(1))
button.place(x=80, y=80)
button2 = tkinter.Button(window, text="Kol 2", command=lambda: gra.klikniecie(2))
button2.place(x=140, y=80)
button3 = tkinter.Button(window, text="Kol 3", command=lambda: gra.klikniecie(3))
button3.place(x=200, y=80)
button4 = tkinter.Button(window, text="Kol 4", command=lambda: gra.klikniecie(4))
button4.place(x=260, y=80)
button5 = tkinter.Button(window, text="Kol 5", command=lambda: gra.klikniecie(5))
button5.place(x=320, y=80)
button6 = tkinter.Button(window, text="Kol 6", command=lambda: gra.klikniecie(6))
button6.place(x=380, y=80)
button7 = tkinter.Button(window, text="Kol 7", command=lambda: gra.klikniecie(7))
button7.place(x=440, y=80)
buttonReset = tkinter.Button(window, text="Reset", command=lambda: gra.restart())
buttonReset.place(x=700, y=700)

przycisk_kolumna = {
    1: button,
    2: button2,
    3: button3,
    4: button4,
    5: button5,
    6: button6,
    7: button7,
}

OPTIONS = [
    "Warunki zwycięstwa Połącz 4",
    "połącz 4 pola swojego koloru nie przedzielone polami koloru przeciwnika:",
    "-pionowo",
    "-poziomo",
    "-po przekątnej",
]

variable = tkinter.StringVar(window)
variable.set(OPTIONS[0])

w = tkinter.OptionMenu(window, variable, *OPTIONS)
w.place(x=520, y=120)

if __name__ == '__main__':
    tkinter.mainloop()
