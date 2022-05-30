"""
This program replicates the popular game Wordle. Text only.
The game indicates a guess's letter is in the correct position by converting it to upper-case.
An asterick (*) beside a letter means that letter is in the answer,
But not at its position within the player's guess.
"""

import random
import string

print(
    "\nThis is a word guessing game. "
    "The word that I'm thinking of has five letters. Enter 'q' to quit."
)

##### VARIABLES
with open("words.txt", encoding="utf-8") as w:
    rawText = w.readlines()
    possibleAnswers = [word[:-1] for word in rawText]
secretAnswer = random.choice(possibleAnswers)
secretLetters = list(secretAnswer)
NUM_TRIES = 0
guessLog = []
wrongLetters = []
availLetters = list(string.ascii_lowercase)

##### GAME START
while NUM_TRIES < 5:
    guess = input("\nEnter your five-letter guess here: ")
    if guess == "q":
        break
    if guess == "skip":
        print(
            f'Skipping to the end of the game. The answer was "{secretAnswer.lower()}".\n'
        )
        break
    if len(guess) != 5:
        print("Oops! That wasn't a five-letter guess. Try again!\n")
        continue
    if guess.title() not in possibleAnswers:
        print("Sorry, that word isn't an option. Try again.")
        continue
    if guess.lower() == secretAnswer.lower():
        print("\nCongratulations! You won the game.\n")
        break
    ### Majority of the game
    NUM_TRIES = NUM_TRIES + 1
    guessLetters = list(guess)
    i = 0
    for l in guessLetters:
        if l == secretLetters[i]:  ### Letter in answer at correct position
            guessLetters[i] = guessLetters[i].upper()
        else:
            if l in secretLetters:  ### Letter in answer at incorrect position
                guessLetters[i] = l + "*"
            else:  ### Letter not in answer
                wrongLetters.append(l)
                if l in availLetters:
                    availLetters.remove(l)
        i += 1
    guessLog.append(guessLetters)
    for log in guessLog:
        print(log)
    print(
        f"\nThese letters are wrong: {wrongLetters}\nThese letters are available: {availLetters}"
    )

if NUM_TRIES == 5:
    print(
        f'\nSorry, you lose! The answer was "{secretAnswer.lower()}". Better luck next time!\n'
    )
