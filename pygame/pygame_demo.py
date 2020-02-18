import sys, pygame

pygame.init()

dimensions = width, height = 800, 800
speed = [2, 2]
black = 0, 0, 0

# create a display surface object
screen = pygame.display.set_mode(dimensions)

# load image surface object
frog = pygame.image.load("frog sprite.png")

# specify rectangle on display surface object for image surface to blit to
frogrect = frog.get_rect()

# resize frog image
frog = pygame.transform.scale(frog, (100, 100))


# fill background of screen black (redundant here, but variable black represents a tuple for background color)
background = screen.fill(black)


""" 
option 1: 
blit (copy) image surface object (frog) onto display surface object (frogrect)
(positions frog at top left of frog rect) 
screen.blit(frog, frogrect) 
"""

""" 
option 2: 
blit frog to general display surface object (screen) and enter rect coordinates for frog to be blitted to) 
** ask about rect coordinates 
"""
screen.blit(frog, (350, 700, 150, 150))

""" animation 
for x in range(100):
    screen.blit(screen, frogrect, frogrect)
    frogrect = frogrect.move(2,0)
    screen.blit(frog, frogrect)
    pygame.display.update()
    pygame.time.delay(100)
"""




# update frog rect
pygame.display.update(frogrect)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()