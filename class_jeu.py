
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
    


class Carte():
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





# class Carte_mouvement(object):
# 	    mouvement = False #vas passer True si une carte bouge

# 	    carte_en_mouvement = [] #liste qui vas contenir les cartes en mouvements
# 	    card_d = ()
# 	    cards = None
# 	    def click_up(self,deck_list):
# 		"""This is used when the user release the mouse button."""
# 		if len(self.carte_en_mouvement) > 0:
# 		    for item in deck_list:      
# 		        if not isinstance(item,Deck_2):
# 		            if item.check_pos() and item.check_card(self.carte_en_mouvement):
# 		                item.add_card(self.carte_en_mouvement)
# 		                self.mouvement = False
# 		                self.carte_en_mouvement = []
# 		                if isinstance(self.cards,Deck_1):
# 		                    self.cards.show_card()
# 		                self.cards = None
# 		                break
# 		    else:
# 		        self.cards.add_card(self.carte_en_mouvement)
# 		        self.mouvement = False
# 		        self.carte_en_mouvement = []
# 		        self.cards = None

# 	    def draw(self,screen,card_dict):
# 		"""This draw the mouvement cards onto the screen"""
# 		if self.mouvement:
# 		    pos = pygame.mouse.get_pos()
# 		    x = pos[0] - self.card_d[0]
# 		    y = pos[1] - self.card_d[1]
# 		    for item in self.mouvement_card:
# 		        screen.blit(card_dict[item],[x,y])
# 		        y += 32
	    