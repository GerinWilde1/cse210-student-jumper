import random
from game.Shoot import glider


word = "HAPPINESS"
reveal = list(len(word)*'_')
lives =4 
won = False


def letter_check(letter, word):
    for i in range(0,len(word)):
        letter = word[i]
        if guess == letter:
            reveal[i] = guess
    if '_' not in reveal:
        return True
    else:
        return False


def show():
    print(glider[4 - lives])
    print(reveal)

while won == False and lives > 0:
    show()
    guess = input('guess letter: ')
    guess = guess.upper()
    
    if guess == word:
        won = True
        reaveal = word
    if len(guess) == 1 and guess in word:
        won = letter_check(guess, word)   
    else:
        lives-=1
    show()

    




    if won:
        print(f"nice! you guessed {word}")
    else:
        print("sorry, loser")