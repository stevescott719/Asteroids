import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: " + str(SCREEN_WIDTH) + "\nScreen height: " + str(SCREEN_HEIGHT))

if __name__ == "__main__":
    main()
