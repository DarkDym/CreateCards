from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity
from pokemontcgsdk.ability import Ability
from pokemontcgsdk.ancienttrait import AncientTrait
from pokemontcgsdk.attack import Attack
from pokemontcgsdk.cardimage import CardImage
from pokemontcgsdk.legality import Legality
from pokemontcgsdk.querybuilder import QueryBuilder
from pokemontcgsdk.resistance import Resistance
from pokemontcgsdk.tcgplayer import TCGPlayer
from pokemontcgsdk.cardmarket import Cardmarket
from pokemontcgsdk.weakness import Weakness
from pokemontcgsdk import RestClient
import json


class Cards:
    def __init__(self):
        self.path_file = "C:/Users/Dymytry/Documents/CreateCards/all_cards.json"
        print("CARDS INITIALIZED!")

    def download_all_cards_json(self):
        RestClient.configure('398ea8f1-720c-418e-9f18-1e80f4ab5e17')
        print("VOU PEGAR AS CARTAS")
        cards = Card.all()
        all_cards = []
        for card in cards:
            card_raw = card.__dict__

            aux_l = []
            try:
                for x in card_raw['attacks']:
                    aux_l.append(x.__dict__)
                card_raw['attacks'] = aux_l
            except TypeError as e:
                card_raw['attacks'] = None

            aux_l = []
            try:
                for x in card_raw['ancientTrait']:
                    aux_l.append(x.__dict__)
                card_raw['ancientTrait'] = aux_l
            except TypeError as e:
                card_raw['ancientTrait'] = None

            aux_l = []
            try:
                for x in card_raw['abilities']:
                    aux_l.append(x.__dict__)
                card_raw['abilities'] = aux_l
            except TypeError as e:
                card_raw['abilities'] = None

            aux_l = []
            try:
                for x in card_raw['resistances']:
                    aux_l.append(x.__dict__)
                card_raw['resistances'] = aux_l
            except TypeError as e:
                card_raw['resistances'] = None

            aux_l = []
            try:
                for x in card_raw['weaknesses']:
                    aux_l.append(x.__dict__)
                card_raw['weaknesses'] = aux_l
            except TypeError as e:
                card_raw['weaknesses'] = None

            try:
                card_raw['cardmarket'] = card_raw['cardmarket'].__dict__
                card_raw['cardmarket']['prices'] = card_raw['cardmarket']['prices'].__dict__
            except AttributeError as e:
                card_raw['cardmarket'] = None


            try:
                card_raw['images'] = card_raw['images'].__dict__
            except TypeError as e:
                card_raw['images'] = None
            
            
            try:
                card_raw['legalities'] = card_raw['legalities'].__dict__
            except TypeError as e:
                card_raw['legalities'] = None
            

            try:
                card_raw['set'] = card_raw['set'].__dict__
                card_raw['set']['images'] = card_raw['set']['images'].__dict__
                card_raw['set']['legalities'] = card_raw['set']['legalities'].__dict__
            except TypeError as e:
                card_raw['set'] = None


            try:
                card_raw['tcgplayer'] = card_raw['tcgplayer'].__dict__
                card_raw['tcgplayer']['prices'] = card_raw['tcgplayer']['prices'].__dict__
                if card_raw['tcgplayer']['prices']['normal'] != None:
                    card_raw['tcgplayer']['prices']['normal'] = card_raw['tcgplayer']['prices']['normal'].__dict__
                if card_raw['tcgplayer']['prices']['holofoil'] != None:
                    card_raw['tcgplayer']['prices']['holofoil'] = card_raw['tcgplayer']['prices']['holofoil'].__dict__
                if card_raw['tcgplayer']['prices']['reverseHolofoil'] != None:
                    card_raw['tcgplayer']['prices']['reverseHolofoil'] = card_raw['tcgplayer']['prices']['reverseHolofoil'].__dict__
                if card_raw['tcgplayer']['prices']['firstEditionHolofoil'] != None:
                    card_raw['tcgplayer']['prices']['firstEditionHolofoil'] = card_raw['tcgplayer']['prices']['firstEditionHolofoil'].__dict__
                if card_raw['tcgplayer']['prices']['firstEditionNormal'] != None:
                    card_raw['tcgplayer']['prices']['firstEditionNormal'] = card_raw['tcgplayer']['prices']['firstEditionNormal'].__dict__
            except AttributeError as e:
                card_raw['tcgplayer'] = None

            all_cards.append(card_raw)

        with open("all_cards.json", "w") as outfile:
            json.dump(all_cards, outfile, indent=4)
        outfile.close()

    def read_cards_json(self):
        with open(self.path_file, 'r', encoding='utf-8') as inputfile:
            self.all_cards = json.load(inputfile)
        inputfile.close()

        return self.all_cards
