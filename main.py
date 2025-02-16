import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print("Pygame running? ", pygame.get_init())
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # add player object to groups

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        #player.update(dt)
        #player.draw(screen)

        # switch to groups to manage game objects
        for game_obj in updatable: 
            game_obj.update(dt)

        for game_obj in drawable:
            game_obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) # restrict fps to 60fps and return time in milliseconds
        dt = dt / 1000 # convert milliseconds to seconds

if __name__ == '__main__':
    main()
