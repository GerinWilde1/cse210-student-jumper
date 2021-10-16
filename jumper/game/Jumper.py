
import random
from game.word import Word 



"""We need the logic to choose which picture gets displayed
If they get a correct letter or a wrong one."""






class Jumper:
    

    def __init__(self):      
      

      x = self.Word.word()
      self.shoot = {                  
      4: """
                  ___  
                  /___\ 
                  \   / 
                  \ /               
                    0   
                  /|\  
                  / \  
              
                ^^^^^^^""",

      3:"""                 
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

      1:"""          
                  \ /  
                    0   
                  /|\  
                  / \  

                ^^^^^^^""",

      0:"""

                    x   
                  /|\  
                  / \  
              
                ^^^^^^^"""}
      
      self.rand = self.Word.word()#picks a random word from the word list
      self.reveal = list(len(self.word)*'_')#creates a panal to demonstrate the amount of letters the user must guess

      
      print(glider[4- self.lives])
      print(self.reveal)

    
    def shot(self, lives):
      lives = 0
      if self.lives == 0:
        print(self.shoot[0])
      elif self.lives == 1:
        print(self.shoot[1])
      elif self.lives == 2:
        print(self.shoot[2])
      elif self.lives == 3:
        print(self.shoot[3])
      elif self.lives == 4:
        print(self.shoot[4])   

    def guess_letter(word, guessed_list):
      """This function lets the user guess a letter and prints out correct ones"""
      # self.reveal is our gussed_list in this function
      # sel.word is our word from in this function
      # we created test.py to show how the function would be working
      print()
      guessed_letter = input("Guess a letter [a-z]: ").lower()

      word_length = len(word) 
      lives = 4
      
      if guessed_letter








      # while lives < word_length:
      #   if count == 4:
      #       break
      #   if word[count] == guessed_letter:
          
      #     guessed_list[count] = guessed_letter
          
      #   count += 1
      
      print()

      for i in guessed_list:
        print(i, end=" ")

      print()

      return guessed_list




    

    