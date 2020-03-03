import sys, pygame

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DIMENSIONS = WIDTH, HEIGHT = 800, 800

screen = pygame.display.set_mode(DIMENSIONS)
background = screen.copy()


class Frog(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("frog sprite.png").convert(), (100, 100))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

    def move_right(self):
        old_rect = self.rect
        screen.blit(background, self.rect, self.rect)
        self.rect = self.rect.move(25, 0)
        screen.blit(self.image, self.rect)
        return old_rect, self.rect

    def move_left(self):
        screen.blit(background, self.rect, self.rect)
        old = self.rect
        self.rect = self.rect.move(-50, 0)
        screen.blit(self.image, self.rect)
        return old, self.rect


class Tile(pygame.sprite.Sprite):
    def __init__(self, x_position: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("counter_sprite.png").convert(), (200, 150))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x_position, 650)


class Game(object):
    def __init__(self):
        self.running = True
        self.popcorn_score = True
        tile_group = [Tile(180), Tile(180), Tile(360), Tile(540), Tile(720), Tile(0)]
        for tile in tile_group:
            background.blit(tile.image, tile.rect)
        screen.blit(background, background.get_rect())
        self.frog = Frog()
        self.frog.rect = self.frog.rect.move(300, 550)
        screen.blit(self.frog.image, self.frog.rect)
        pygame.display.update()

    def move_frog(self):
        changed_areas = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            old_rect, new_rect = self.frog.move_left()
            changed_areas.extend([old_rect, new_rect])
        elif keys[pygame.K_RIGHT]:
            old_rect, new_rect = self.frog.move_right()
            changed_areas.extend([old_rect, new_rect])
        pygame.display.update(changed_areas)
        pygame.time.delay(30)


def main():
    running = True
    pygame.init()

    '''tile_group = [Tile(180), Tile(180), Tile(360), Tile(540), Tile(720), Tile(0)]
    for tile in tile_group:
        background.blit(tile.image, tile.rect)
    screen.blit(background, background.get_rect())

    frog = Frog()
    frog.rect = frog.rect.move(300, 550)
    screen.blit(frog.image, frog.rect)

    pygame.display.flip()
    '''
    game = Game()

    while game.running:
        game.move_frog()
        '''
        changed_areas = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            old_rect, new_rect = frog.move_left()
            changed_areas.extend([old_rect, new_rect])
        elif keys[pygame.K_RIGHT]:
            old_rect, new_rect = frog.move_right()
            changed_areas.extend([old_rect, new_rect])
        pygame.display.update(changed_areas)
        pygame.time.delay(30)
        '''


if __name__ == "__main__":
    main()
