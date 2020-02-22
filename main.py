import pygame 
import json
from creation_deck import *
from interface import * 
import pygame

pygame.init()

LARGEUR = 800 
HAUTEUR = 1200
gameDisplay = pygame.display.set_mode((HAUTEUR,LARGEUR))
blanc = (255,255,255)
noir = (0,0,0)

rouge = (200,0,0)
vert = (0,200,0)

rouge_clair = (255,0,0)
vert_clair = (0,255,0)

clock = pygame.time.Clock()

def quitgame():
    pygame.quit()
    quit()


def text_objects(text, font):
    textSurface = font.render(text, True, noir)
    return textSurface, textSurface.get_rect()

def crash():
    message_display('le jeu a crasher')

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((HAUTEUR/2),(LARGEUR/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


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



def GameDisplay():
  
    crash = False

    while not crash:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = True


        gameDisplay.fill(blanc)
        pygame.display.update()
        clock.tick(60)






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


def game_loop():
    


    

game_menu()
GameDisplay()