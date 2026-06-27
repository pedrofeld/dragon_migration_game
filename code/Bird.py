from code.Entity import Entity

class Bird(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.speed = 1

    def flee(self):
        pass

    def update(self):
        pass