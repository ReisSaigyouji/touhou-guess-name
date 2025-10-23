import random

names = ["REIMU", "MARISA", "RUMIA", "CIRNO", "DAIYOUSEI", "MEILING",
         "KOAKUMA", "PATCHOULI", "SAKUYA", "REMILIA", "FLANDRE"]

def game():
    name = random.choice(names)
    guess = '_' * len(name)
    used = []
    print("Guess the name, it has", len(name), "letters.")
    while guess != name:
        print(guess)
        letter = input("Guess a letter: ").upper()
        print(letter)
        if letter in used:
            print("You already tried that letter!")
        elif len(letter) != 1:
            print("Please enter a single letter.")
        elif letter in name:
            new = ""
            print("Correct!")
            for i in range(len(name)):
                if letter == name[i]:
                    new += letter
                else:
                    new += guess[i]
            guess = new
            used.append(letter)
        else:
            print("There is no such letter!")
            used.append(letter)
    print(f"That's right! It's {name}")


def main():
    choice = ''
    while choice != '0':
        choice = input("""Welcome to character guessing game!
        Choose one of the options:
        Play - 1
        Exit - 0
        Your choice: """)
        if choice == '1':
            game()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid input.")


if __name__ == '__main__':
    main()