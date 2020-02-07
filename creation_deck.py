
import random
import json



class Carte():
    def __init__(self,dmg_monstre,hp_monstre,hp_4invoc,name_monstre ,sprite_path):
        self.dmg_monstre = dmg_monstre
        self.hp_monstre = hp_monstre
        self.hp_4invoc = hp_4invoc
        self.name_monstre = name_monstre
        self.sptite_path = sprite_path

    def __repr__(self):
        return "{}".format(self.name_monstre)






def cree_deck():
    deck1 = []
    deck2 = []
    with open('data.json') as fichier:
        data = json.load(fichier)
        for carte_id, card_data in data.items():
            carte = Carte(**card_data)
            deck1.append(carte)
            deck2.append(carte)
        melange_deck(deck1,deck2)
        test_deck(deck1,deck2)


        

def melange_deck(deck1,deck2):
    random.shuffle(deck1)
    random.shuffle(deck2)

def test_deck(deck1,deck2):
    print(deck1)
    print(len(deck1))

    print(deck2)
    print(len(deck2))




cree_deck()

