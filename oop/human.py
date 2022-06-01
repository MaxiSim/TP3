import random
from player import Player

class Human(Player):
    def __init__(self, name, xy, weapon = None, face = '@', hit_points = 50, tool = None, treasure = None):
        super().__init__(name, xy, face, weapon = weapon, hit_points = hit_points)
        self.tool = tool
        self.treasure = treasure
        
    def has_tool(self, tool):
        self.tool = tool[0]
        
    def has_treasure(self, treasure):
        self.treasure = treasure[0]
        
    def get_tool(self):
        return self.tool
    def get_treasure(self):
        return self.treasure

    def damage(self):
        return self._damage(10)
