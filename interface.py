import pygame

pygame.init()


ecran_hauteur = 800
ecran_largeur = 1500

ecran = pygame.display.set_mode((ecran_largeur,ecran_hauteur))

carte1 = pygame.image.load('sprite_cartes/1.png')

pygame.display.set_caption('test')

timer = pygame.time.Clock()








def carte(x,y):
    
    ecran.blit(carte1,(x,y))

x = 250
y = 200

x_change = 0










game_crash = False

while not game_crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_crash = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_change = -5
            if event.key == pygame

    
    carte(x,y)
    pygame.display.update()
    timer.tick(60)

pygame.quit()
quit()
