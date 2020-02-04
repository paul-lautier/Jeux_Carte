import json


# fonction pour récuperer les infos des cartes en fonction de leur ID :
def get_dmg(id_carte):
    
    with open('data.json') as fichier:
        data = json.load(fichier)
    
    for carte in data[id_carte]:
        return(carte['dmg_monstre'])



def get_hp(id_carte):
    
    with open('data.json') as fichier:
        data = json.load(fichier)
    
    for carte in data[id_carte]:
        return(carte['hp_monstre'])


def get_name_monstre(id_carte):
    
    with open('data.json') as fichier:
        data = json.load(fichier)
    

    for carte in data[id_carte]:
        return(carte['name_monstre'])


def get_hp_4invoc(id_carte):
    
    with open('data.json') as fichier:
        data = json.load(fichier)
    

    for carte in data[id_carte]:
        return(carte['hp_4invoc'])


def get_sprite(id_carte):
        
    with open('data.json') as fichier:
        data = json.load(fichier)
    

    for carte in data[id_carte]:
        return(carte['sprite_path'])

