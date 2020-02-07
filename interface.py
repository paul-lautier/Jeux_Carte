import pygame
import matplotlib


def cree_ecran():
    pygame.init()

    blanc = (255,255,255)

    

    ecranH = 1000
    ecranL = 1700

    carteH = 100
    carteL = 80

    ecran = pygame.display.set_mode((ecranL,ecranH))
    pygame.display.set_caption("coeur de pierre")


    timer = pygame.time.Clock()
    game_over = False



    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        ecran.fill(blanc)
        pygame.display.update()

    

    pygame.quit()
    quit()



