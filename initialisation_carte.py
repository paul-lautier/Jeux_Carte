import json


def cree_carte(carte_id):

    with open('data.json') as fichier:
        data = json.load(fichier)
    

    for carte in data[carte_id]:
        print(carte)




# cree_carte("2")