from pokemontcgsdk import Set
from pokemontcgsdk import RestClient
import json
import os
from AllCards import Cards
import requests
from credentials import credentials

class Sets:
    def __init__(self, flag_cdir=False):
        self.path_file = "C:/Users/Dymytry/Documents/CreateCards/all_sets.json"
        self.path_base = "C:/Users/Dymytry/Documents/CreateCards/"
        self.cards = Cards()
        self.flag_cdir = flag_cdir
        self.list_props = {'props' : ['Foil','Promo','Pre Release','Reverse Foil','Staff']}
        self.list_qlty = {'qlty' : ['NM','SP','MP','HP','D']}
        self.list_lang = {'lang' : ['ENG','PTBR']}
        print("SETS INITIALIZED!")

    def download_sets(self):
        self.tcg_api_key = credentials()
        RestClient.configure(self.tcg_api_key.key)

        sets = Set.all()
        all_sets = []

        for set in sets:
            sets_raw = set.__dict__

            sets_raw['images'] = sets_raw['images'].__dict__

            sets_raw['legalities'] = sets_raw['legalities'].__dict__

            try:
                sets_raw['ptcgoCode'] = sets_raw['ptcgoCode'].__dict__
            except AttributeError as e:
                sets_raw['ptcgoCode'] = None

            all_sets.append(sets_raw)

        with open("all_sets.json", "w") as outfile:
            json.dump(all_sets, outfile, indent=4)
        outfile.close()

    def get_all_sets(self):
        with open(self.path_file, 'r', encoding='utf-8') as inputfile:
            self.all_sets = json.load(inputfile)
        inputfile.close()

        self.list_sets = []

        for set in self.all_sets:
            self.list_sets.append(set['series'])
        
        # print(self.list_sets)

        self.list_unq_sets = []

        for elem in self.list_sets:
            if elem not in self.list_unq_sets:
                self.list_unq_sets.append(elem)

        print(self.list_unq_sets)
        return self.list_unq_sets

    def get_sub_sets(self):
        
        self.all_subsets = []
        self.aux_all_subsets = []
        self.t = []
        
        for subset in self.list_unq_sets:
            for set in self.all_sets:
                if subset == set['series']:
                    self.aux_all_subsets.append(set['id'])
            self.all_subsets.append(self.aux_all_subsets)
            #t_aux = {'name' : set, 'subset' : self.aux_all_subsets}
            #self.t.append(t_aux)
            self.aux_all_subsets = []
        print(self.all_subsets)

        '''
        Somente para a criação das pastas. Caso seja necessário a criação das pastas,
        na inicialização da classe Sets, passar o valor de flag_cdir para True. Caso
        contrário manter False.
        '''
        if self.flag_cdir:
            for elem in range(0,len(self.list_unq_sets)):
                self.list_unq_sets[elem] = self.list_unq_sets[elem].replace(' & ' , '_')

        print(self.list_unq_sets)
        return self.all_subsets

    def adjust_sets_to_qt(self):
        self.block = self.get_all_sets()
        self.subsets = self.get_sub_sets()
        set = []
        for x in range(0, len(self.block)):
            set.append({'name' : self.block[x], 'subset' : self.subsets[x]})
        qt_set = {'set' : set}
        print(qt_set)
        return qt_set

    def return_cards_to_qt(self, id):
        self.allCards = self.cards.read_cards_json()
        cards_json = []
        for x in self.allCards:
            if id == x['set']['id']:
                c = {'name' : x['name'], 'number' : x['number'], 'set_id': x['set']['id'], 'set_series': x['set']['series']}
                cards_json.append(c)

        return sorted(cards_json, key=lambda x: int(x['number']) if x['number'].isdigit() else float('inf'))

    def create_dir_sets(self):
        for dir in self.list_unq_sets:
            path = os.path.join(self.path_base, dir)

            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Dir Created: {path}")
            else:
                print(f"Dir already created: {path}")
        
        for i in range(0,len(self.list_unq_sets)):
            path = os.path.join(self.path_base, self.list_unq_sets[i])
            for x in self.all_subsets[i]:
                sub_path = os.path.join(path, x)
                if not os.path.exists(sub_path):
                    os.makedirs(sub_path)
                    print(f"SubDir Created: {sub_path}")
                else:
                    print(f"SubDir already created: {sub_path}")

    def set_logo_download(self):
        '''
        Nesta função vai ser baixado todos os logos e ícones de cada uma dos blocos
        e das coleções internas.
        '''

        
        pass
    
    def download_and_store_all_cards_images(self):
        
        self.all_cards = self.cards.read_cards_json()


        '''
        Separar todas as cartas pelo set delas, assim deixar em uma lista
        onde cada uma das cartas vai ter quer ser baixada com o número referente a carta
        e salva na pasta referente ao set dela.
        '''

        erro = 1
        total_cartas = 0

        for set in self.list_unq_sets:
            for card in self.all_cards:
                # total_cartas+=1
                if card['set']['series'] == set:                    
                    # print(self.list_unq_sets)
                    # print(e)

                    '''
                    Workaround por causa do nome das coleções em relação aos nomes das pastas
                    '''
                    aux_set = set
                    if ' & ' in set:
                        aux_set = set.replace(' & ' , '_')

                    url = card['images']['small']                    
                    dir = os.path.join(self.path_base, aux_set)
                    sub_dir = os.path.join(dir, card['set']['id'])
                    file_name = str(card['number']) + "_s.png"
                    aux_path = os.path.join(sub_dir, file_name)
                    if os.path.exists(aux_path):
                        print(f"A imagem {aux_path} já foi baixada!")
                    else:
                        resp = requests.get(url)
                        if resp.status_code == 200:
                            try:
                                with open(aux_path, "wb") as arquivo:
                                    arquivo.write(resp.content)
                                print("Imagem baixada e salva com sucesso em:", aux_path)
                            except OSError as e:
                                print(f"Erro no nome da imagem, o nome vai virar {aux_set}+{erro}")
                                file_name = str(aux_set) + "_" + str(erro) + "_s.png"                    
                                aux_path = os.path.join(sub_dir, file_name)
                                erro+=1
                                with open(aux_path, "wb") as arquivo:
                                    arquivo.write(resp.content)
                                print("Imagem baixada e salva com sucesso em:", aux_path)
                        else:
                            print("Erro ao baixar a imagem. Código de status:", resp.status_code)
                            print(f"URL da imagem que não foi baixada: {url}")




#s = Sets()
#s.get_all_sets()
#s.get_sub_sets()
# s.create_dir_sets()
#s.download_and_store_all_cards_images()
