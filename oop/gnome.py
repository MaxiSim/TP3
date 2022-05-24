import random
from player import Player

class Gnome(Player):
    def __init__(self, name, xy, weapon = None, face = 'G', hit_points = 50):
        super().__init__(name, xy, face, weapon = weapon, hit_points = hit_points)
        
    def damage(self):
        return self._damage(5)
