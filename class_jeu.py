from initialisation_carte import *
import json

class joueur():
    def __init__(self, nom_invocateur):
        self.hp_invocateur = 30
        self.nom_invocateur = nom_invocateur
        self.heal_invocateur = heal_invocateur
        self.heal_point = heal_point

    def invoc(self,invocateur):
        self.hp_invocateur -= hp_4invoc

    def heal_invocateur(self,invocateur):
        self.hp_invocateur += heal_point
    


class carte():
    def __init__(self):
        self.dmg_monstre = get_dmg(1)
        self.hp_monstre = get_hp(1)
        self.hp_4invoc = get_hp_4invoc(1)
        self.name_monstre = get_name_monstre(1)
        
    

    def attack_player(self,nom_monstre):
        self.hp_invocateur -= dmg_monstre
    def attack_monstre(self,nom_monstre):
        self.dmg_monstre -= hp_monstre


def test():
    dragon = carte()
    print(dragon.hp_monstre)

test()