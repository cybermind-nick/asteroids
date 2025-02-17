import pygame
from constants import *
from circleshape import *

import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):

        pygame.draw.circle(screen, "white",  self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill() # always kill first

        if self.radius <= ASTEROID_MIN_RADIUS: # if it was the smallest type, no need to respawn, just return
            return
        else: # Needs to spawn smaller asteroids
            random_angle = random.uniform(20, 50)

            vector_a = self.velocity.rotate(random_angle)
            vector_b = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_1.velocity = vector_a * 1.2

            asteroid_2.velocity = vector_b * 1.2
