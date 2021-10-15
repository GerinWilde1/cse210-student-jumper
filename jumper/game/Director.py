import game.Jumper as jumper
import game.word as word
import game.console as console



class Director:


    def __init__(self):
        self.keep_playing = True
        self.console = console()
        self.jumper = jumper()
        self.word = word()

        

    def start_game(self):

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        letter = self.console.read_letter("Guess a letter [a-z]: ")
        self.word.choice(letter)

    def do_outputs(self):
        pass
    def do_updates(self):
        pass