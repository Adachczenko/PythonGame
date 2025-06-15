class Player:
    def __init__(self, name, health=100, score=0):
        self.name = name
        self.health = health
        self.score = score

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def add_score(self, points):
        self.score += points

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Player(name={self.name}, health={self.health}, score={self.score})"