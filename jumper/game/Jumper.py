from game.words2 import words 
from game.Shoot import glider
import random



class Jumper:
          
          
          def __init__(self):
                    
                    
                    lives = 4
                    self.word  = random.choice(words)#picks a random word from the word list
                    self.reveal = list(len(self.word)*'_')#creates a panal to demonstrate the amount of letters the user must guess
 
                   
                    print(glider[4- lives])
                    print(self.reveal)
