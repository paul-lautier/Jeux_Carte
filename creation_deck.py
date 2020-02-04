from initialisation_carte import *
deck_joueur1 = []
deck_joueur2 = []
deck_complet = []


class carte():
    def __init__(self,dmg_monstre,hp_monstre,hp_4invoc,name_monstre):
        self.dmg_monstre = dmg_monstre
        self.hp_monstre = hp_monstre
        self.hp_4invoc = hp_4invoc
        self.name_monstre = name_monstre

    def __str__(self):
        return ""






def cree_carte(id_carte):
     with open('data.json') as fichier:
        data = json.load(fichier)
        for dmg_monstre in data:
            for hp_monstre in data:
                for name_monstre in data:
                    for hp_4invoc in data:
                        deck_complet.append(carte(dmg_monstre,hp_monstre,name_monstre,hp_4invoc))

    
     



def ajouter_au_deck():
    deck_joueur1 = deck_complet
    deck_joueur2 = deck_complet



def melange_deck(deck_joueur1,deck_joueur2):
    pass

#founction de test des deck
def test_deck():
    print(deck_joueur1)
    print(len(deck_joueur1))
    print(deck_joueur2)
    print(len(deck_joueur2))


cree_carte("1")
ajouter_au_deck()
test_deck()


