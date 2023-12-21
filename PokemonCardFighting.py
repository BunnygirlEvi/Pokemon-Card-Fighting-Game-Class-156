from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title("Pokemon Card Fighting Game")
root.geometry("600x600")

pikachu = ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
abra = ImageTk.PhotoImage(Image.open ("abra.jpg"))
bulbasaur = ImageTk.PhotoImage(Image.open ("bulbasaur.jpg"))
abra = ImageTk.PhotoImage(Image.open ("abra.jpg"))
ivysaur = ImageTk.PhotoImage(Image.open ("Ivysaur.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open ("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open ("paras.jpg"))
persian = ImageTk.PhotoImage(Image.open ("persian.jpg"))
rattata = ImageTk.PhotoImage(Image.open ("rattata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open ("squirtle.jpg"))

button1 = ImageTk.PhotoImage(Image.open ("button1.png"))
button2 = ImageTk.PhotoImage(Image.open ("button2.png"))

root.configure(background = "#fca903")


player1 = Label(root, text = "Player 1", bg = "#fc3503", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player1_score_label = Label(root, bg = "#fc3503", fg = "white")
player1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "#0373fc", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player2_score_label = Label(root, bg = "#0373fc", fg = "white")
player2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_card_label = Label(root, bg = "white", fg = "black")
random_card_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()