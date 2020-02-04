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
    def __init__(self,dmg_monstre,hp_monstre,hp_4invoc,name_monstre):
        self.dmg_monstre = dmg_monstre
        self.hp_monstre = hp_monstre
        self.hp_4invoc = hp_4invoc
        self.name_monstre = name_monstre


        
    
    # fonction d'attaque de monstre sur joueur :
    def attack_player(self,nom_monstre):
        self.hp_invocateur -= dmg_monstre

    # fonction d'attaque de monstre sur monstre :
    def attack_monstre(self,nom_monstre):
        self.dmg_monstre -= hp_monstre

# fonction de test de print de carte
def test():
    dragon = carte()
    print("dmg ",dragon.dmg_monstre)
    print("name ",dragon.name_monstre)
    print("for invoc ",dragon.hp_4invoc)
    print("hp ",dragon.hp_monstre)
    print("sprite",dragon.sprite_path)

test()