from code.Entity import Entity

class Dragon(Entity):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.max_hp = 100
        self.score = 0

    def move(self):
        pass

    def eat_bird(self):
        pass

    def take_damage(self, damage):
        pass

    def heal(self):
        pass