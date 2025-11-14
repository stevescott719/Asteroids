import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from circleshape import CircleShape
from player import Player

def main():
    
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: " + str(SCREEN_WIDTH) + "\nScreen height: " + str(SCREEN_HEIGHT))
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.time.Clock
    dt = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                return

        screen.fill("black")

        player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

        player.draw(screen)

        pygame.display.flip()

        dt = pygame.time.Clock().tick(60) / 1000

        #print(f"Delta time: {dt:.4f} seconds")


if __name__ == "__main__":
    main()
