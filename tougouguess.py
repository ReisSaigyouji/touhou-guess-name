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
        self.used = []
        # state of word
        self.word_label = tk.Label(root, text=" ".join(self.guess), font=("Arial", 24))
        self.word_label.pack(pady = 10)
        # input
        self.entry = tk.Entry(root, font=("Arial", 18), width=5)
        self.entry.pack()
        self.entry.focus()
        # funny button
        self.button = tk.Button(root, text="guess", command=self.check_letter)
        self.button.pack(pady = 5)
        # message field
        self.message_label = tk.Label(root, text=" ", font=("Arial", 14))
        self.message_label.pack(pady=10)

    def check_letter(self):
        letter = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if not letter.isalpha() or len(letter) != 1:
            self.message_label.config(text="Please enter a single letter.")
            return

        if letter in self.used:
            self.message_label.config(text="You already tried that letter!")
            return

        self.used.append(letter)

        if letter in self.name:
            self.message_label.config(text="Correct!")
            new = ""
            for i in range(len(self.name)):
                if letter == self.name[i]:
                    new += letter
                else:
                    new += self.guess[i]
            self.guess = new
            self.word_label.config(text=" ".join(self.guess))

            if self.guess == self.name:
                self.message_label.config(text=f"That's right! It's {self.name}")
                self.button.config(state=tk.DISABLED)
        else:
            self.message_label.config(text="There is no such letter!")



if __name__ == "__main__":
    root = tk.Tk()
    game = GameGUI(root)
    root.mainloop()
