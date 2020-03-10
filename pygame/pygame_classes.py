import sys, pygame, random

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
        self.rect = self.rect.move(-25, 0)
        screen.blit(self.image, self.rect)
        return old, self.rect

    def move_up(self):
        screen.blit(background, self.rect, self.rect)
        old = self.rect
        self.rect = self.rect.move(0, -25)
        screen.blit(self.image, self.rect)
        return old, self.rect

    def move_down(self):
        screen.blit(background, self.rect, self.rect)
        old = self.rect
        self.rect = self.rect.move(0, 50)
        screen.blit(self.image, self.rect)
        return old, self.rect

    def gravity(self):
        screen.blit(background, self.rect, self.rect)
        old = self.rect
        self.rect = self.rect.move(0, 7)
        screen.blit(self.image, self.rect)
        return old, self.rect


class Tile(pygame.sprite.Sprite):
    def __init__(self, x_position: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("counter_sprite.png").convert(), (200, 150))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x_position, 650)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x_position: int, y_position: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("tile_sprite.png").convert(), (200, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x_position, y_position)

class Candy(pygame.sprite.Sprite):
    def __init__(self, x_position: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("candy_sprite.png").convert(), (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x_position, -50)

    def update(self):

        screen.blit(background, self.rect, self.rect)
        old = self.rect
        self.rect = self.rect.move(0, 20)
        screen.blit(self.image, self.rect)
        return old, self.rect




class Game(object):
    def __init__(self):
        self.candy_list = []
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
        self.timer_max = 100
        self.timer = 1

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
        elif keys[pygame.K_UP]:
            old_rect, new_rect = self.frog.move_up()
            changed_areas.extend([old_rect, new_rect])
        pygame.display.update(changed_areas)
        pygame.time.delay(30)

    def gravity(self):
        changed_areas = []
        if self.frog.rect.top < 550:
            old_rect, new_rect = self.frog.gravity()
            changed_areas.extend([old_rect, new_rect])
        pygame.display.update(changed_areas)
        pygame.time.delay(30)

    def update_timer(self):
        if self.timer <= self.timer_max:
            self.timer += 1
        else:
            self.timer = 1

    def spawn_candy(self):
        if self.timer % 100 == 0:
            candy = Candy(random.randint(0, 800))
            self.candy_list.append(candy)
            background.blit(candy.image, candy.rect)
            screen.blit(background, background.get_rect())
            screen.blit(self.frog.image, self.frog.rect)
            print("Make candy")

    def move_candy(self):
        changed_area = []
        for candy in self.candy_list:
            old_rect, new_rect = candy.update()
            changed_area.extend([old_rect, new_rect])
            pygame.display.update(changed_area)
            pygame.time.delay(30)
            print("Candy")



def main():
    running = True
    pygame.init()
    game = Game()

    while game.running:
        game.gravity()
        game.move_frog()
        game.spawn_candy()
        game.update_timer()
        game.move_candy()



if __name__ == "__main__":
    main()

# ask about this^
