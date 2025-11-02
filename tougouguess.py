import random
import tkinter as tk

names = ["REIMU", "MARISA", "RUMIA", "CIRNO", "DAIYOUSEI", "MEILING",
         "KOAKUMA", "PATCHOULI", "SAKUYA", "REMILIA", "FLANDRE", "LETTY", "CHEN", "LILY", "CHEN", "ALICE",
         "MERLIN", "LYRICA", "LUNASA", "YOUMU", "YUYUKO", "RAN", "YUKARI"]

class GameGUI:
    def __init__(self, root):
        self.root = root
        root.title("Touhou Guessing Game")
        root.geometry("400x260")
        root.resizable(False, False)
        # general things
        self.name = random.choice(names)
        self.guess = "_" * len(self.name)
        self.used = []
        self.lives = 5

        # lives
        self.lives_label = tk.Label(root, text="❤️" * self.lives, font=("Arial", 18))
        self.lives_label.pack(anchor="ne", padx=10, pady=10)
        # state of word
        self.word_label = tk.Label(root, text=" ".join(self.guess), font=("Arial", 24))
        self.word_label.pack(pady = 10)
        # input
        self.entry = tk.Entry(root, font=("Arial", 18), width=5)
        self.entry.pack()
        self.entry.focus()
        # submit button
        self.button = tk.Button(root, text="guess", command=self.check_letter)
        self.button.pack(pady = 5)
        # message field
        self.message_label = tk.Label(root, text=" ", font=("Arial", 14))
        self.message_label.pack(pady=10)
        # play again button
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)
        self.play_again_button.pack_forget()  # hide it for now

        # the thing so the Enter works as submit
        self.entry.bind('<Return>', lambda event: self.check_letter())


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
                self.play_again_button.pack() # show the play again button
        else:
            self.lives -= 1
            self.update_hearts()
            if self.lives == 0:
                self.message_label.config(text=f"You lost! The name was {self.name}")
                self.button.config(state="disabled")
                self.play_again_button.pack()
            else:
                self.message_label.config(text="There is no such letter!")

    # added all that so you can replay without restarting everything
    def reset_game(self):
        self.name = random.choice(names)
        self.guess = "_" * len(self.name)
        self.used = []
        # reset display
        self.word_label.config(text=" ".join(self.guess))
        self.message_label.config(text="")
        self.button.config(state=tk.NORMAL)
        self.play_again_button.pack_forget()
        self.entry.delete(0, tk.END)
        self.entry.focus()
        # lives reset
        self.lives = 5
        self.lives_label.config(text=f"Lives: {self.lives}")
        self.update_hearts()

    # to display lives
    def update_hearts(self):
        self.lives_label.config(text="❤️" * self.lives)


# It's done finally yey yippie
if __name__ == "__main__":
    root = tk.Tk()
    game = GameGUI(root)
    root.mainloop()
