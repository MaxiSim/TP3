import random
from player import Player

class Gnome(Player):
    def __init__(self, name, xy, weapon = None, face = 'G', hit_points = 50, tool = None):
        super().__init__(name, xy, face, weapon = weapon, hit_points = hit_points)
        self.tool = tool
        
    def get_tool(self):
        return self.tool
    
    def damage(self):
        return self._damage(5)
