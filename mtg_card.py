

class mtg_card():
    def __init__(self, library_path):

        with open(library_path) as mtg_lib:
            card_library = json.load(mtg_lib)
        
        self.library = card_library