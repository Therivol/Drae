

class Health:
    def __init__(self, entity, maximum, regen):
        self.entity = entity
        self.current = maximum
        self.maximum = maximum
        self.regen_rate = regen

    def hit(self, value):
        if self.current - value <= 0:
            self.dead()
        else:
            self.current -= value

    def heal(self, value):
        if self.current + value > self.maximum:
            self.current = self.maximum
        else:
            self.current += value

    def dead(self):
        pass
