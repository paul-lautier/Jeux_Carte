import pygame

blanc = (255,255,255)

pygame.init()

ecranH = 500
ecranL = 500

carteH = 50
carteL = 50

ecran = pygame.display.set_mode((ecranL,ecranH))
pygame.display.set_caption("coeur de pierre")


game_over = False

while not game_over :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    ecran.fill(blanc)
    pygame.display.update()

pygame.quit()
quit()


