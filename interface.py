import tkinter
from tkinter.constants import DISABLED

import game


def utworz_kolko(canv, x, y, r):
    """
    Eysowanie koła
    :param canv:
    :param x: Wspolrzedna x
    :param y:
    :param r:
    :return: id kolka
    """
    return canv.create_oval(x - r, y - r, x + r, y + r)


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
    "Reguły",
    "Zasada 1",
    "asdadadsjkdsdjknjkfgasfjk asdklfhjasjklfdjklfbasf dsfkjahsfhdjkas sdkjfhaskjdfh sadkjfksdjfh afkdsj hkljh",
    "asdadadsjkdsdjknjkfgasfjk asdklfhjasjklfdjklfbasf dsfkjahsfhdjkas sdkjfhaskjdfh sadkjfksdjfh afkdsj hkljh",
    "Zasada 2",
]

variable = tkinter.StringVar(window)
variable.set(OPTIONS[0])

w = tkinter.OptionMenu(window, variable, *OPTIONS)
w.place(x=520, y=120)

tkinter.mainloop()
