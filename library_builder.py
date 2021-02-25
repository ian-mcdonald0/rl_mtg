import json
import requests

class library_builder():
    def __init__(self, library_path, card_name):

        with open(library_path) as mtg_lib:
            card_library = json.load(mtg_lib)

        self.card_library = card_library
        self.library_path = library_path
        self.card_name = card_name


        self.check_library()



    def check_library(self):
        '''
        Checks to see if card is in downloaded library. If not then adds card to json library
        '''

        if self.card_name in self.card_library.keys():
            print(f'{self.card_name} already in library')
        else:
            self.add_card_to_library()
            print(f'{self.card_name} added to library')



        # def generate_card_from_library(card_info):

    def add_card_to_library(self):
        api_name = self.card_name.replace(' ','+')
        r = requests.get("https://api.scryfall.com/cards/named?fuzzy="+ api_name)
        
        card_info_json = json.loads(r.text)
        card_summary_json = {'name': card_info_json['name'],
                             'mana_cost': card_info_json['mana_cost'],
                             'cmc': card_info_json['cmc'],
                             'type': card_info_json['type_line'],
                             'power': card_info_json['power'],
                             'toughness': card_info_json['toughness'],
                             'colors': card_info_json['colors'],
                             'keywords': card_info_json['keywords'],
                             'details': card_info_json['oracle_text']}

        self.card_library[self.card_name] = card_summary_json
        with open(self.library_path, 'w') as outfile:
            json.dump(self.card_library, outfile)

