import sys

import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # add player object to groups
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        #player.update(dt)
        #player.draw(screen)

        # switch to groups to manage game objects
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player): # player collision check
                print("Game over!")
                sys.exit(0)

            for bullet in shots: # bullet collision check
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()

        for game_obj in drawable:
            game_obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) # restrict fps to 60fps and return time in milliseconds
        dt = dt / 1000 # convert milliseconds to seconds

if __name__ == '__main__':
    main()
