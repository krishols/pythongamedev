import sys, pygame
pygame.init()

dimensions = width, height = 800, 800
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(dimensions)

frog = pygame.image.load("frog sprite.png")
frogrect = frog.get_rect()
frog = pygame.transform.scale(frog, (100,100))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()



    screen.fill(black)
    screen.blit(frog, frogrect)
    pygame.display.flip()