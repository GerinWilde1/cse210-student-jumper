
import random
from game.words2 import words 
from game.Shoot import glider



"""We need the logic to choose which picture gets displayed
If they get a correct letter or a wrong one."""






class Jumper:
    

    def __init__(self):      
        lives = 4
        self.word  = random.choice(words)#picks a random word from the word list
        self.reveal = list(len(self.word)*'_')#creates a panal to demonstrate the amount of letters the user must guess

        
        print(glider[4- lives])
        print(self.reveal)

    def shoot(self):
        shoot = {                  
        0: """
                    ___  
                   /___\ 
                   \   / 
                    \ /               
                     0   
                    /|\  
                    / \  
                
                  ^^^^^^^""",

        1:"""                 
                   /___\ 
                   \   / 
                    \ /  
                     0   
                    /|\  
                    / \  
                            
                  ^^^^^^^""",
                        
        2:"""          
                   \   / 
                    \ /  
                     0   
                    /|\  
                    / \  

                  ^^^^^^^""",

        3:"""          
                    \ /  
                     0   
                    /|\  
                    / \  

                  ^^^^^^^""",

        4:"""

                     x   
                    /|\  
                    / \  
                
                  ^^^^^^^"""}