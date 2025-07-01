from re import A
import pygame
import sys
from code.constants import *
from code.player import Player
from code.asteroid import Asteroid
from code.asteroidfield import AsteroidField
from code.shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # object containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    # initialisation
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen,"black")
        
        dt = clock.tick(60)
        dt /= 60
        
        #player.draw(screen)
        for thing in drawable:
            thing.draw(screen)
        #player.update(dt)
        for thing in updatable:
            thing.update(dt)
        
        pygame.display.flip()
            
        for asteroid in asteroids:
            if asteroid.collision_occurred(player):
                print("Game over!")
                sys.exit()
                
        for asteroid in asteroids:        
            for shot in shots:
                if asteroid.collision_occurred(shot):
                    shot.kill()
                    asteroid.split()
                    
        



if __name__ == "__main__":
    main()
