import pygame
import sys
from game import Game  # Dodano import klasy Game

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Game")
clock = pygame.time.Clock()

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    running = True
    game = Game()  # Inicjalizacja obiektu Game

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game.stop()  # Zatrzymanie gry

        # Logika gry
        game.update()

        # Rysowanie
        screen.fill(WHITE)
        game.render(screen)  # Wywołanie renderowania gry

        # Aktualizacja ekranu
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()