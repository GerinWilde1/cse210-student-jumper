import random
from game.Shoot import glider
from game.word import Word


choice = Word()
word = choice.word()
reveal = list(len(word)*'_')
lives = 4
won = False
lose = False


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

while won == False and lives != 0:
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

    if won:
        print(f"nice! you guessed {word}")
        print("")
    else:
        print("sorry, loser")
        print(" ")
if lives == 0:
    lose = True
if lose == True:
    print(glider[4])
    print("You've lost")
    lost = False

