import pygame 
import json
import random
from creation_deck import *
from class_jeu import *





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
        TextSurf, TextRect = text_objects("Jeu De Cartes", largeText)
        TextRect.center = ((HAUTEUR/2),(LARGEUR/2))
        gameDisplay.blit(TextSurf, TextRect)

        bouton("START",150,450,100,50,vert,vert_clair,game_loop)
        bouton("QUITTER",550,450,100,50,rouge,rouge_clair,quitgame)
    

        pygame.display.update()
        clock.tick(15)


def game_screen():
    game=True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()







    pygame.display.update()



#boucle du jeu 
def game_loop():

    # game_screen()

    #vérif de début de jeu
    rules_ok = False
    game_running = False

    #tours des joueurs
    joueur1_tour = False
    joueur2_tour = False

    #def des variables de cartes
    card_on_board1=[]
    card_on_board2=[]
    dead_card=[]

    #def des variables de jeu
    pose_carte=False
    passe_tour=False
    attaque=False



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
            print(str(joueur1.nom_invocateur),"commence")
        else:
            joueur1_tour = False
            joueur2_tour = True
            print(str(joueur2.nom_invocateur),"commence")


        while (joueur1.hp_invocateur != 0 or joueur2.hp_invocateur != 0):
            if joueur1_tour:
                keys = pygame.key.get_pressed()
                for event in pygame.event.get():
        
                    #choix de l'action a éffectuer ce tour
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pose_carte = True
                            print("appuyez sur la touche numerique qui correspond au numéro de la carte pour la posé")

                        if event.key == pygame.K_w:
                            attaque = True
                            print("appuyez sur la touche numerique qui correspond au numéro de la carte pour attaquer avec")

                        if event.key == pygame.K_e:
                            passe_tour = True
                            print("vous avez passer votre tour")


                if passe_tour :
                    joueur1_tour = False
                    joueur2_tour = True

                        

                    
                if attaque and len(card_on_board1) != 0:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            card_on_board1[0].attack_monstre( )

                    pass     
                        
                        


                if pose_carte == True and len(card_on_board1) < 5:
                    if event.type == pygame.KEYDOWN :

                        if event.key == pygame.K_1:
                            card_on_board1.append(main1.pop(0))
                            print(card_on_board2)
                            pose_carte=False

                        if event.key == pygame.K_2:
                            card_on_board1.append(main1.pop(1))
                            pose_carte=False

                        if event.key == pygame.K_3:
                            card_on_board1.append(main1.pop(2))
                            pose_carte=False

                        if event.key == pygame.K_4:
                            card_on_board1.append(main1.pop(3))
                            pose_carte=False

                        if event.key == pygame.K_5:
                            card_on_board1.append(main1.pop(4))
                            pose_carte=False
                    




                

   


            if joueur2_tour:

                keys = pygame.key.get_pressed()
                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pose_carte = True
                            print("appuyez sur la touche numerique qui correspond au numéro de la carte pour la posé")

                        if event.key == pygame.K_w:
                            attaque = True
                            print("appuyez sur la touche numerique qui correspond au numéro de la carte pour attaquer avec")

                        if event.key == pygame.K_e:
                            passe_tour = True
                            print("vous avez passer votre tour")
                            


                if passe_tour:
                    joueur1_tour = True
                    joueur2_tour = False
                    


                if pose_carte == True and len(card_on_board2)<5:
                    
                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_1:
                                card_on_board2.append(main2.pop(0))
                                print(card_on_board2)
                                pose_carte=False

                            if event.key == pygame.K_2:
                                card_on_board2.append(main2.pop(1))
                                pose_carte=False

                            if event.key == pygame.K_3:
                                card_on_board2.append(main2.pop(2))
                                pose_carte=False

                            if event.key == pygame.K_4:
                                card_on_board2.append(main2.pop(3))
                                pose_carte=False

                            if event.key == pygame.K_5:
                                card_on_board2.append(main2.pop(4))
                                pose_carte=False
                        else:
                            print('votre terrain de jeu est déjà remplie')


                    
                

                        




    

    


    

game_menu()
GameDisplay()