import pygame, random

#initialize pygame
pygame.init()

#create display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Group Collide!")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#define classes
class Game():
    """A class to help manage and run our game"""
    def __init__(self, monster_group, knight_group):
      self.monster_group = monster_group
      self.knight_group = knight_group

    def update(self):
         self.check_collisions()
         
    def check_collisions(self):
        pygame.sprite.groupcollide(self.monster_group, self.knight_group, True, False)


class Knight(pygame.sprite.Sprite):
    """A simple class to represent a knight"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    def update(self):
        """update and move the monster"""
        self.rect.y -= self.velocity

class Monster(pygame.sprite.Sprite):
    """A simple class to represent a spooky monster"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("blue_monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    def update(self):
        """update and move the monster"""
        self.rect.y += self.velocity

#Create a monster group
my_monster_group = pygame.sprite.Group()
for i in range(12):
    monster = Monster(i*64, 10)
    my_monster_group.add(monster)

#create a knight group
my_knight_group = pygame.sprite.Group()
for i in range(12):
   knight = Knight(i*64, WINDOW_HEIGHT-64)
   my_knight_group.add(knight)

#create a game object
my_game = Game(my_monster_group, my_knight_group)



#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the surface
    display_surface.fill((0, 0 , 0))

    #update and draw sprite groups
    my_monster_group.update()
    my_monster_group.draw(display_surface)

    my_knight_group.update()
    my_knight_group.draw(display_surface)

    #update the game
    my_game.update()

    #update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#end the game
pygame.quit()



