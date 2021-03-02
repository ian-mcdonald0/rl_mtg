from .mtg_card import mtg_card
from .library_builder import library_builder

class hand():
    def __init__(self, library_path, card_list):

        # Cards in hand
        self.cards = dict()

        # instantiating cards and putting them in the hand
        for card_name in card_list:
            library_builder(library_path, card_name)
            self.cards[card_name] = mtg_card(library_path, card_name)
