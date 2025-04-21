import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init(self, x, y, radius):
        super().init(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) 

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            split_v1 = self.velocity.rotate(split_angle)
            split_v2 = self.velocity.rotate(-split_angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, split_radius)

            asteroid1.velocity = split_v1 * 1.2
            asteroid2.velocity = split_v2 * 1.2
