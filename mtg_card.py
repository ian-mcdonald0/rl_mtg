import json

class mtg_card():
    def __init__(self, library_path, card_name):

        with open(library_path) as mtg_lib:
            card_library = json.load(mtg_lib)
        
        self.library = card_library

        card_info = self.library[card_name]

        self.name = card_name
        self.mana_cost: card_info['mana_cost']
        self.cmc = card_info['cmc']
        self.type = card_info['type_line']
        self.power = card_info['power']
        self.toughness = card_info['toughness']
        self.colors = card_info['colors']
        self.keywords = card_info['keywords']
        self.details = card_info['oracle_text']


        self.tapped = False
        self.played = False

                
    def fake(self):
        pass