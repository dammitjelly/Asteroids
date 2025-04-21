import pygame
from player import *
from constants import *
from asteroid import *
from shot import *
from asteroidfield import *

def main():
    pygame.init()
    print(
        "Starting Asteroids!\n"
        f"Screen width: {SCREEN_WIDTH}\n"
        f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    gr_updatable = pygame.sprite.Group()
    gr_drawable = pygame.sprite.Group()
    gr_asteroids = pygame.sprite.Group()
    gr_shots = pygame.sprite.Group()

    Player.containers = (gr_updatable, gr_drawable)
    Asteroid.containers = (gr_updatable, gr_drawable, gr_asteroids)
    AsteroidField.containers = (gr_updatable)
    Shot.containers = (gr_updatable, gr_drawable, gr_shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ast_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        gr_updatable.update(dt)
        for obj in gr_drawable:
            obj.draw(screen)
        
        for asteroid in gr_asteroids:
            for bullet in gr_shots:
                if asteroid.collides_with(bullet):
                    asteroid.split()
                    bullet.kill()
            
            if asteroid.collides_with(player):
                print("Game Over!")
                exit()
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()