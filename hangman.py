# Write your code here
import random
print("H A N G M A N")
while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'play':
        lst = ["python", "java", "kotlin", "javascript"]
        word = random.choice(lst)
        hint = "-" * len(word)
        hint_list = list(hint)
        i = 0
        guess = []
        while i < 8:
            print()
            print(hint)
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print("You should input a single letter")
                continue
            if letter in guess:
                print("You've already guessed this letter")
                continue
            else:
                guess.append(letter)
            if letter in word:
                index = 0
                if letter in hint:
                    print("No improvements")
                    i += 1
                    continue
                for val in word:
                    if val == letter:
                        hint_list[index] = letter
                    index += 1
                hint = "".join(hint_list)
            elif not letter.islower():
                print("Please enter a lowercase English letter")
                continue
            else:
                print("That letter doesn't appear in the word")
                i += 1
            if "-" not in hint:
                break
        if "-" in hint:
            print("You lost!")
        else:
            print("You guessed the word!\nYou survived!")
    elif menu == 'exit':
        break
    else:
        continue
