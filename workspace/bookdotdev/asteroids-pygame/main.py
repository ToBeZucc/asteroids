import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot

def main():
    pygame.init() #Initiate pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Setting screen width and height
    clock = pygame.time.Clock() #Clock created for fps purposes
    dt = 0.0 #Create a Delta Time variable
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create and Position the Player

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField() # Creates the Asteroid Field

    Shot.containers = (shots, drawable, updatable)

    while True: #Creating game loop
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") #Fill screen with Black
        updatable.update(dt) #Update the postion of every sprite in the Payer(updatable) group

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        for shape in drawable:
            shape.draw(screen) #Draw each object int the drawable group

        pygame.display.flip() #Display update
        dt = clock.tick(60) / 1000 # Added FPS Limiter


if __name__ == "__main__":
    main()
