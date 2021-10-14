import random, string

class Jumper:
          

          def __init__(self):
                    self.needed_letter = random.choice(string.ascii_letters)
                    print(self.needed_letter)
Jumper()