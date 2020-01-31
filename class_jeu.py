

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
    def __init__(self, carte_id):
        self.dmg_monstre = dmg_monstre
        self.hp_monstre = hp_monstre
        self.hp_4invoc = hp_4invoc
        self.nom_monstre = name_monstre
        self.heal_monstre = heal_monstre
    

    def attack_player(self,nom_monstre):
        self.hp_invocateur -= dmg_monstre

    def attack_monstre(self,nom_monstre):
        dmg_monstre -= hp_monstre
    

    

