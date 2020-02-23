import pygame 
import json
from creation_deck import *
from class_jeu import *
import pygame


'''
INITIALISATION PYGAME
'''
pygame.init()
clock = pygame.time.Clock()

'''
DIMENSION ECRAN 
'''
LARGEUR = 800 
HAUTEUR = 1200
gameDisplay = pygame.display.set_mode((HAUTEUR,LARGEUR))


'''
COULEURS
'''
blanc = (255,255,255)
noir = (0,0,0)
rouge = (200,0,0)
vert = (0,200,0)
rouge_clair = (255,0,0)
vert_clair = (0,255,0)



'''
FONCTION INTERFACE
'''


#fonction d'arrêt d'une fenêtre
def quitgame():
    pygame.quit()
    quit()


def text_objects(text, font):
    textSurface = font.render(text, True, noir)
    return textSurface, textSurface.get_rect()

#fonction pour écrire du texte
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((HAUTEUR/2),(LARGEUR/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

#fonction de création de bouton
def bouton(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

#création de la fenêtre de jeu 
def GameDisplay():
  
    crash = False

    while not crash:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = True


        gameDisplay.fill(blanc)
        pygame.display.update()
        clock.tick(60)

#menu du jeu
def game_menu():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(blanc)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((HAUTEUR/2),(LARGEUR/2))
        gameDisplay.blit(TextSurf, TextRect)

        bouton("START",150,450,100,50,vert,vert_clair,game_loop)
        bouton("QUITTER",550,450,100,50,rouge,rouge_clair,quitgame)
    

        pygame.display.update()
        clock.tick(15)



#boucle du jeu 
def game_loop():

    #vérif de début de jeu
    rules_ok = False
    game_running = False

    #tours des joueurs
    joueur1_tour = False
    joueur2_tour = False


    #import des decks + main + pioche des deux joueurs
    deck1, deck2 = cree_deck()
    main1, main2 = cree_main_joueur(deck1,deck2)
    pioche1, pioche2 = cree_pioche(deck1,deck2)

    #vérification de l'état des decks + main + pioche
    if len(main1) == 5 and len(main2) == 5 and len(pioche1) == 15 and len(pioche2) == 15 :
        rules_ok = True
        game_running = True 

    #si état decks en règles création des instances de joueurs
    if rules_ok == True :
        joueur1 = joueur("paul",main1,pioche1)
        joueur2 = joueur("pierre",main2,pioche2)
        print('jeu rdy')

    #si decks en règles début du jeu
    while game_running:

        # choix du tour 
        turn = random.randint(1,2) # pile ou face 
        if turn == 1:
            joueur1_tour = True
            joueur2_tour = False
            print("\nle joueur 1 commence.")
        else:
            joueur1_tour = False
            joueur2_tour = True
            print("\nle joueur 2 commence.")


        while (joueur1.hp_invocateur != 0 or joueur2.hp_invocateur != 0):
            if joueur1_tour:
                pass


    



    


    

game_menu()
GameDisplay()