
import random
from game.word import Word
import game.Shoot as Shoot



"""We need the logic to choose which picture gets displayed
If they get a correct letter or a wrong one."""






class Jumper:
    

    def __init__(self):      
      

      x = self.Word.word()

      self.lives = 4
      self.rand = self.Word.word()#picks a random word from the word list
      self.reveal = list(len(self.word)*'_')#creates a panal to demonstrate the amount of letters the user must guess

      
      print(glider[4- self.lives])
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
    
    def guess_letter(word, guessed_list):
      """This function lets the user guess a letter and prints out correct ones"""
      # self.reveal is our gussed_list in this function
      # sel.word is our word from in this function
      # we created test.py to show how the function would be working
      print()
      guessed_letter = input("Guess a letter [a-z]: ").lower()

      guessed_list = guessed_list 
      word_length = len(word) 
      count = 0
      
      while count < word_length:
        if count > word_length:
            break
        if word[count] == guessed_letter:
          
          guessed_list[count] = guessed_letter
          
        count += 1
      
      print()

      for i in guessed_list:
        print(i, end=" ")

      print()

      return guessed_list


    

    