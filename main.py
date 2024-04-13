import tkinter as tk
from tkinter import ttk
import main_menu

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

class App(tk.Tk):
    def __init__(self, title, dimensions):
        super().__init__()
        
        #Main Setup
        self.title(title)
        self.geometry(f'{dimensions[0]}x{dimensions[1]}')
        self.minsize(dimensions[0],dimensions[1])

        #Widgets
        self.menu = main_menu.Menu(self)

        #Main Loop
        self.mainloop()


# path_file = "C:/Users/Dymytry/Desktop/PCCA/alL_cards.json"

# with open(path_file, 'r', encoding='utf-8') as inputfile:
#     all_cards = json.load(inputfile)



# for card in all_cards:

















# aux_l.clear()
# for x in card_raw['images']:
#     aux_l.append(x.__dict__)
# card_raw['images'] = aux_l


# print(card_raw['attacks'])
#print(card_raw['attacks'][0].__dict__)
# print(card_raw)
# categories = ["abilities","artist","ancientTrait","attacks","cardmarket",
#               "convertedRetreatCost","evolvesFrom","flavorText","hp","id",
#               "images","legalities","regulationMark","name","nationalPokedexNumbers",
#               "number","rarity","regulationMark","resistances","retreatCost","rules",
#               "set","subtypes","supertype","tcgplayer","types","weaknesses"]


# # print(card.__dict__)
# cards = Card.all()
# print("PEGUEI AS CARTAS")

# with open("all_card.txt", "w", encoding="utf-8") as outfile:
#     for item in cards:
#         outfile.write(str(item) + '\n')

# outfile.close()




# main_windown = App('Main', (800,600))
        
# Abrir o arquivo de texto
# caminho_arquivo = 'C:/Users/Dymytry/Desktop/PCCA/all_card2.txt'
# caminho_arquivo_NEW = 'C:/Users/Dymytry/Desktop/PCCA/all_card2.txt'

# with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
#     # Ler cada linha e colocá-las em uma lista
#     linhas = arquivo.readlines()
# arquivo.close()

# # Remover quebras de linha (\n) de cada linha, se necessário
# linhas = [linha.strip() for linha in linhas]



# with open(caminho_arquivo_NEW, 'w', encoding='utf-8') as arquivo:
#     # Ler cada linha e colocá-las em uma lista
#     for x in linhas:
#         aux = "[" + x
#         aux = aux[:-1]
#         arquivo.write(aux + '\n')    
# arquivo.close()



# # Converter a lista em um dicionário
# dados = {'linhas': linhas}

# # Converter o dicionário em uma representação JSON
# json_str = json.dumps(dados, indent=4)

# # Salvar o JSON em um arquivo
# caminho_json = 'dados.json'

# with open(caminho_json, 'w') as arquivo_json:
#     arquivo_json.write(json_str)

# print("Arquivo JSON criado com sucesso!")        