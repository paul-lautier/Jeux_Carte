import pygame

pygame.init()


ecran_hauteur = 800
ecran_largeur = 800

ecran = pygame.display.set_mode((ecran_largeur,ecran_hauteur))

startImage = pygame.image.load('logo/start.png')

pygame.display.set_caption('test')

timer = pygame.time.Clock()

def start(x,y):
    ecran.blit(startImage,(x,y))

x = (ecran_largeur * 0.45)
y = (ecran_hauteur * 0.8)



game_crash = False

while not game_crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_crash = True
    
    start(x,y)
    pygame.display.update()
    timer.tick(60)

pygame.quit()
quit()
