from class_jeu import *
import random
import json
from fonction_jeu import *

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
        # test_deck(deck1,deck2)
        cree_main_joueur(deck1,deck2)
        # test_deck(deck1,deck2)
        cree_pioche(deck1,deck2)
        # test_deck(deck1,deck2)
        


        

def melange_deck(deck1,deck2):
    random.shuffle(deck1)
    random.shuffle(deck2)

def test_deck(deck1,deck2):
    print("deck du joueur 1 : ",deck1)
    print(len(deck1))

    print("deck du joueur 2 : ",deck2)
    print(len(deck2))





cree_deck()
