import random
import tkinter as tk

names = ["REIMU", "MARISA", "RUMIA", "CIRNO", "DAIYOUSEI", "MEILING",
         "KOAKUMA", "PATCHOULI", "SAKUYA", "REMILIA", "FLANDRE"]

class GameGUI:
    def __init__(self, root):
        self.root = root
        root.title("Touhou Guessing Game")

        self.name = random.choice(names)
        self.guess = "_" * len(self.name)
        # state of word
        self.word_label = tk.Label(root, text=" ".join(self.guess), font=("Arial", 24))
        self.word_label.pack(pady = 10)
        # input
        self.entry = tk.Entry(root, font=("Arial", 18), width=5)
        self.entry.pack()
        self.entry.focus()


