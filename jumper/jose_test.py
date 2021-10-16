import random



word = "HAPPINESS"
reveal = list(len(word)*'_')
lives =4 
won = False

while won == False and lives > 0:
    print(reveal)
    guess = input('guess letter: ')
    guess = guess.upper()
    
    if guess == word:
        won = True
    if len(guess) == 1 and guess in word:
        for i in range(0,len(word)):
            letter = word[i]
            if guess == letter:
                reveal[i] = guess
            if '_' not in reveal:
                won = True
    
    
    else:
        lives-=1


    
    if won:
        print("nice!")
    else:
        print("sorry, loser")