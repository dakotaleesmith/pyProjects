import random
import string

print(f"\nThis is a word guessing game. The word that I'm thinking of has five letters. Enter 'q' to quit.")

##### VARIABLES
with open('wordle_clone/words.txt') as w:
    rawText = w.readlines()
    possibleAnswers = [word[:-1] for word in rawText]
secretAnswer = random.choice(possibleAnswers)
secretLetters = list(secretAnswer)
numTries = 0
guessLog = []
wrongLetters = []
availLetters = list(string.ascii_lowercase)

##### GAME START
while numTries < 5:
    guess = input("\nEnter your five-letter guess here: ") 
    if guess == 'q':
        break
    elif guess == 'skip':
        print(f'Skipping to the end of the game. The answer was "{secretAnswer.lower()}".\n')
        break
    elif len(guess) != 5:
        print("Oops! That wasn't a five-letter guess. Try again!\n")
        continue
    elif guess.title() not in possibleAnswers:
        print("Sorry, that word isn't an option. Try again.")
        continue
    elif guess.lower() == secretAnswer.lower():
        print("\nCongratulations! You won the game.\n")
        break
    else: ### Majority of the game occurs in this loop
        numTries = numTries + 1
        guessLetters = list(guess)
        i = 0
        for l in guessLetters:
            if l == secretLetters[i]: guessLetters[i] = guessLetters[i].upper() ### Letter in answer at correct position
            else:
                if l in secretLetters: guessLetters[i] = l + '*' ### Letter in answer at incorrect position
                else: ### Letter not in answer
                    wrongLetters.append(l)
                    if l in availLetters: availLetters.remove(l)
            i += 1    
    guessLog.append(guessLetters)
    for log in guessLog: print(log)
    print(f"\nThese letters are wrong: {wrongLetters}\nThese letters are available: {availLetters}")

if numTries == 5:
    print(f'\nSorry, you lose! The answer was "{secretAnswer.lower()}". Better luck next time!\n')
