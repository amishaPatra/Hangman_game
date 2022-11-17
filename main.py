import random
from ascii_art import logo

print(logo)
from ascii_art import stages

from words import word_list

chosen_word = random.choice(word_list)
#tprint("word is: " + chosen_word)
word_length = len(chosen_word)

display = []
for i in range(word_length):
    display.append("_")

lives = 6

end_game = False

while not end_game:


    print(display)
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You have already entered this letter.l")


    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not a letter in the word")
        print(stages[lives])
        print(f"You are left with {lives} lives")

    if "_" not in display:
        end_game = True
        print(display)
        print("You win!")


    elif lives == 0:
        end_game = True
        if "_" not in display:
            print(display)
            print("You win!")
        else:
            print(display)
            print("You lose!")
            print(f"Your word was '{chosen_word}'")

