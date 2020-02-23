from class_jeu import *
import random
import json



'''
CRÉATION DU DECK
'''
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


    return deck1,deck2




'''
CRÉATION DE LA MAIN DU JOUEUR
'''

def cree_main_joueur(deck1,deck2):
    main1 = []
    main2 = []

    for a in range (5):
        main1.append(deck1.pop(a))
        main2.append(deck2.pop(a))

    test_main(main1,main2)
    return main1,main2


'''
CRÉATION DE LA PIOCHE
'''
def cree_pioche(deck1,deck2):
    pioche1 = []
    pioche2 = []

    while len(deck1) != 0 :
        pioche1.append(deck1.pop(0))
        pioche2.append(deck2.pop(0))

    # test_pioche(pioche1,pioche2)
    return pioche1,pioche2
        



        


'''
GESTION DES CARTES
'''
def melange_deck(deck1,deck2):
    random.shuffle(deck1)
    random.shuffle(deck2)

def pioche(pioche_joueur,main_joueur):
    for une in range(1):
        main_joueur.append(pioche_joueur.remove(une))

def del_carte(main_joueur,carte_rm):
    main_joueur.remove(carte_rm)



'''
FONCTION DE TEST
'''

def test_deck(deck1,deck2):
    print("deck du joueur 1 : ",deck1)
    print(len(deck1))

    print("deck du joueur 2 : ",deck2)
    print(len(deck2))


def test_pioche(pioche1,pioche2):
    print("pioche du joueur 1 : ", pioche1)
    print(len(pioche1))

    print("pioche du joueur 2 : ",pioche2)
    print(len(pioche2))


def test_main(main1,main2):
    print("main joueur 1 : ",main1)
    print(len(main1))

    print("main joueur 2 : ", main2)
    print(len(main2))
