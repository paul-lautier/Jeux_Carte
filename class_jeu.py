
import json

class joueur(object):
    def __init__(self, nom_invocateur,main_joueur,pioche_joueur):
        self.hp_invocateur = 30
        self.heal_par_tour = 3
        self.nom_invocateur = nom_invocateur
        self.main_joueur= main_joueur
        self.pioche_joueur = pioche_joueur
        

    def invoc(self,invocateur):
        self.hp_invocateur -= hp_4invoc

    def heal_invocateur(self,invocateur):
        self.hp_invocateur += heal_par_tour
    


class Carte(object):
    def __init__(self,dmg_monstre,hp_monstre,hp_4invoc,name_monstre ,sprite_path):
        self.dmg_monstre = dmg_monstre
        self.hp_monstre = hp_monstre
        self.hp_4invoc = hp_4invoc
        self.name_monstre = name_monstre
        self.sprite_path = sprite_path

    def __repr__(self):
        return "{}".format(self.name_monstre)
   
    # fonction d'attaque de monstre sur joueur :
    def attack_player(self,nom_monstre):
        self.hp_invocateur -= dmg_monstre

    # fonction d'attaque de monstre sur monstre :
    def attack_monstre(self,nom_monstre):
        self.dmg_monstre -= hp_monstre
