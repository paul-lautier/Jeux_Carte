import pygame
import matplotlib
from creation_deck import *

carteH = 100
carteL = 80

def path_to_sprite(main1,main2):
    for carte in main1:
        carte.sprite_path = pygame.image.load(str(carte) + ".png")   
        largeur, hauteur = carteL, carteH 
    for carte in main2:
        carte.sprite_path = pygame.image.load(str(carte) + ".png")   
        largeur, hauteur = carteL, carteH 


                

        


def cree_ecran():
    pygame.init()



    ecranH = 1000
    ecranL = 1700

    carteH = 100
    carteL = 80
    
    ecran = pygame.display.set_mode((ecranL,ecranH))
    pygame.display.set_caption("logo/logo.png")


    testX = 250
    testY = 750



    timer = pygame.time.Clock()
    game_over = False


    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        

        pygame.display.update()

    
 
    pygame.quit()
    quit()


cree_deck()
path_to_sprite(main1,main2)
cree_ecran()