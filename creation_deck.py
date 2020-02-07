from initialisation_carte import *
deck_joueur1 = []
deck_joueur2 = []
deck_complet = []


class Carte():
    def __init__(self,dmg_monstre,hp_monstre,hp_4invoc,name_monstre ,sprite_path):
        self.dmg_monstre = dmg_monstre
        self.hp_monstre = hp_monstre
        self.hp_4invoc = hp_4invoc
        self.name_monstre = name_monstre
        self.sptite_path = sprite_path

    def __rept__(self):
        return "{}".format(self.name_monstre)






def cree_carte():
    deck = []
    with open('data.json') as fichier:
        data = json.load(fichier)
        for card_id, card_data in data.items():
            carte = Carte(
                **card_data
                # card_data['dmg_monstre'],
                # card_data['hp_monstre'],
                # card_data['name_monstre'],
                # card_data['hp_4invoc'],
                # card_data['sprite_path']

            )
            

    
     



def ajouter_au_deck():
    for i in range (20) :
        deck_joueur1.append(deck_complet)
        deck_joueur2.append(deck_complet)



def melange_deck(deck_joueur1,deck_joueur2):
    pass

#founction de test des deck
def test_deck():
    # print(deck_joueur1)
    # print(len(deck_joueur1))
    # # print(deck_joueur2)
    # print(len(deck_joueur2))
    print(deck_complet)
    # print(len(deck_complet))


cree_carte()
ajouter_au_deck()
test_deck()


