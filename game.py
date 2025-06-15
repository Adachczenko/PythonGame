from player import Player  # Dodano import klasy Player

class Game:
    def __init__(self):
        self.running = False
        self.player = Player()  # Inicjalizacja obiektu Player

    def start(self):
        self.running = True
        self.run()

    def run(self):
        while self.running:
            self.update()
            self.render()

    def update(self):
        # Aktualizacja stanu gry
        pass

    def render(self):
        # Renderowanie gry
        pass

    def stop(self):
        self.running = False