import json



def get_dmg():
    
    with open('data.json') as fichier:
        data = json.load(fichier)
    

    for carte in data['cartes']:
        print(carte['dmg_monstre'])



def get_hp():
    
    with open('data.json') as fichier:
        data = json.load(fichier)
    

    for carte in data['cartes']:
        print(carte['hp_monstre'])


def get_name_monstre():
    
    with open('data.json') as fichier:
        data = json.load(fichier)
    

    for carte in data['cartes']:
        print(carte['name_monstre'])


def get_hp_4invoc():
    
    with open('data.json') as fichier:
        data = json.load(fichier)
    

    for carte in data['cartes']:
        print(carte['hp_4invoc'])

