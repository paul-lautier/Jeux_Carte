import pygame
import matplotlib


def carte_to_sprite(name_monstre,sprite_path):
    for i in range (20):
        with open('data.json') as fichier:
            data2 = json.load(fichier)
            for carte in main
                pass
                

        


def cree_ecran():
    pygame.init()



    ecranH = 1000
    ecranL = 1700

    carteH = 100
    carteL = 80

    ecran = pygame.display.set_mode((ecranL,ecranH))
    pygame.display.set_caption("logo/logo.png")

    test_sprite = pygame.image.load('sprite_cartes/1.png')
    testX = 250
    testY = 750

    def test():
        ecran.blit(test_sprite, (testX,testY))


    timer = pygame.time.Clock()
    game_over = False


    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        

        
        test()
        pygame.display.update()

    
 
    pygame.quit()
    quit()



cree_ecran()