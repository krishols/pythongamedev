import sys, pygame

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DIMENSIONS = WIDTH, HEIGHT = 800, 800

screen = pygame.display.set_mode(DIMENSIONS)



class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("counter_sprite.png").convert(), (200, 150))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()


def main():
    x = True
    while x:
        pygame.init()
        frog = Frog()
        frog.rect = frog.rect.move(300, 550)
        screen.blit(frog.image, frog.rect)
        tile_group = []
        tile_group.append(Tile())
        tile_group.append(Tile())
        tile_group.append(Tile())
        tile_group.append(Tile())
        tile_group.append(Tile())
        tile_group.append(Tile())
        tile1 = tile_group[0]
        tile2 = tile_group[1]
        tile3 = tile_group[2]
        tile4 = tile_group[3]
        tile5 = tile_group[4]
        tile6 = tile_group[5]
        tile1.rect = tile1.rect.move(180, 650)
        tile2.rect = tile1.rect.move(180, 650)
        tile3.rect = tile3.rect.move(360, 650)
        tile4.rect = tile4.rect.move(540, 650)
        tile5.rect = tile5.rect.move(720, 650)
        tile6.rect = tile6.rect.move(0, 650)
        for tile in tile_group:
            screen.blit(tile.image, tile.rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                x = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("left")
                    frog.move_left()
                if event.key == pygame.K_RIGHT:
                    print("right")
                    frog.move_right()


class Frog(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("frog sprite.png").convert(), (100, 100))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()


    def move_right(self):
        self.rect.x += 25

    def move_left(self):
        screen.blit(screen, self.rect)
        old = self.rect
        self.rect = self.rect.move(-50, 0)
        screen.blit(self.image, self.rect)
        pygame.event.get()
        pygame.display.update([old, self.rect])
        #pygame.time.delay(100)


        """ for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.rect.x -= 25
                if event.key == pygame.K_RIGHT:
                    self.rect.x += 25
            screen.blit(self.image, self.rect)
            """


'''
animate frog
        for y in range(100):
            screen.blit(screen, frog.rect, frog.rect)
            old = frog.rect
            frog.rect = frog.rect.move(10, 0)
            screen.blit(frog.image, frog.rect)
            pygame.event.get()
            pygame.display.update([old, old])
            pygame.time.delay(50)
            pygame.display.flip()

  

        

        speed = [2, 2]
        black = 0, 0, 0

        # create a display surface object
        
        rect = pygame.draw.rect(screen, (255, 0, 0), (50,50,50,50))
        screen.blit(screen,rect)'''

if __name__ == "__main__":
    main()
