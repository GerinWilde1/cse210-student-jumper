




class Director:


    def __init__(self):
        pass
        self.keep_playing = True
        
        

    def start_game(self):

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        pass
    def do_outputs(self):
        pass
    def do_updates(self):
        pass