deck_joueur1 = []
deck_joueur2 = []

carte = "1"
deck_verif = False





def cree_deck():

    while len(deck_joueur1) < 30 and len(deck_joueur2) < 30:
        deck_joueur1.append(carte)
        deck_joueur2.append(carte)
    if len(deck_joueur1) == 30 and len(deck_joueur2) == 30:
        deck_verif = True



cree_deck()#test

print(deck_joueur1)
print(deck_joueur2)