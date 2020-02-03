import json



def get_dmg(id):
    
    with open('data.json') as fichier:
        data = json.load(fichier)
    

    for carte in data['cartes']:
        return(carte['dmg_monstre'])



def get_hp(id_carte):
    
    with open('data.json') as fichier:
        data = json.load(fichier)
    
    for carte in data['cartes']:
        return(carte['hp_monstre'])


def get_name_monstre(id):
    
    with open('data.json') as fichier:
        data = json.load(fichier)
    

    for carte in data['cartes']:
        return(carte['name_monstre'])


def get_hp_4invoc(id):
    
    with open('data.json') as fichier:
        data = json.load(fichier)
    

    for carte in data['cartes']:
        return(carte['hp_4invoc'])

