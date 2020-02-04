from initialisation_carte import *
deck_joueur1 = []
deck_joueur2 = []


class carte():
    def __init__(self,id_carte):
        self.dmg_monstre = get_dmg(id_carte)
        self.hp_monstre = get_hp(id_carte)
        self.hp_4invoc = get_hp_4invoc(id_carte)
        self.name_monstre = get_name_monstre(id_carte)
        # self.sprite_path = get_sprite("1")


# variable de test : 


# vérification de la validité du deck 
deck_verif = False




def cree_carte(id_carte):
    pass




def ajouter_au_deck():

    while len(deck_joueur1) < 20 and len(deck_joueur2) < 20:
        deck_joueur1.append(carte)
        deck_joueur2.append(carte)
    if len(deck_joueur1) == 20 and len(deck_joueur2) == 20:
        deck_verif = True


def melange_deck(deck_joueur1,deck_joueur2):
    pass

#founction de test des deck
def test_deck():
    print(deck_joueur1)
    print(len(deck_joueur1))
    print(deck_joueur2)
    print(len(deck_joueur2))


cree_carte()
ajouter_au_deck()
test_deck()


