import pygame
from constants import *

def main():
    running = True
    pygame.init()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)).fill("Black")
        pygame.display.flip()



if __name__ == "__main__":
    main()