# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

def main():
    word = "beans"
    guessed_list = list(len(word)*"_")
    reveal = list(len(word)*'_ ')
    print(reveal)
    
    guessed_list = guess_letter(word, guessed_list)
    
    guessed_list = guess_letter(word, guessed_list)
    
    guessed_list = guess_letter(word, guessed_list)
    
    guessed_list = guess_letter(word, guessed_list)

    guessed_list = guess_letter(word, guessed_list)

def guess_letter(word, guessed_list):
      """This function lets the user guess a letter and prints out correct ones"""
      print()
      guessed_letter = input("Guess a letter [a-z]: ").lower()

      guessed_list = guessed_list 
      word_length = len(word) 
      count = 0
      
      while count < word_length:
        if count > word_length:
            break
        if word[count] == guessed_letter:
          # if count == 0:
          #   guessed_list.replace(f"{guessed_list[count]}",f"{guessed_letter}") 
          
          # else:
          #   guessed_list.replace(f"{guessed_list[count * 2]}",f"{guessed_letter}")
          guessed_list[count] = guessed_letter
          
        
        count += 1
      
      print()
      for i in guessed_list:
        print(i, end=" ")
      print()

      return guessed_list

if __name__ == "__main__":
    main()