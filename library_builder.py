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

        self.add_card_to_library()
        print(f'{self.card_name} added to library')

        # if self.card_name in self.card_library.keys():
        #     print(f'{self.card_name} already in library')
        # else:
        #     self.add_card_to_library()
        #     print(f'{self.card_name} added to library')



        # def generate_card_from_library(card_info):

    def add_card_to_library(self):
        api_name = self.card_name.replace(' ','+')
        r = requests.get("https://api.scryfall.com/cards/named?fuzzy="+ api_name)

        key_attributes = ['name', 'mana_cost', 'cmc', 'type_line', 'power', 'toughness', 'colors', 'keywords', 'produced_mana', 'oracle_text']
        card_summary_json = {}
        
        card_info_json = json.loads(r.text)
        for attribute in key_attributes:
            if attribute in card_info_json.keys():
                card_summary_json[attribute] = card_info_json[attribute]

            else:
                card_summary_json[attribute] = None

        self.card_library[self.card_name] = card_summary_json
        with open(self.library_path, 'w') as outfile:
            json.dump(self.card_library, outfile, indent=4, sort_keys=True)

