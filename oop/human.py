import random
from player import Player

class Human(Player):
    def __init__(self, name, xy, weapon = None, face = '@', hit_points = 50):
        super().__init__(name, xy, face,  weapon = weapon, hit_points = hit_points)
        self.treasure = None
        self.tool = None

    def damage(self):
        return self._damage(10)
