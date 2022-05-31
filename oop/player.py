import random

class Player:
    def __init__(self, name, xy, face, weapon = None, hit_points=50, tool = None, treasure = None):
        self.name = name
        self.x, self.y = xy
        self._hp = hit_points
        self.max_hp = hit_points
        self.alive = True
        self.face = face
        self.weapon = weapon
        self.tool = tool
        self.treasure = treasure
    
    @property
    def hp(self):
        return f'({self._hp}/{self.max_hp})'
    
    @property
    def location(self):
        return f'({self.x}/{self.y})'
    
    @hp.setter
    def hp(self, value):
        if value > self.max_hp:
            self._hp = self.max_hp
        else:
            self._hp = value

    def loc(self):
        return self.x, self.y

    def move_to(self, xy):
        self.x, self.y = xy
        
        
    def kill(self):
        self.hp = 0
        self.alive = False
    
    def _damage(self, dmg):
        if self.weapon == 'sword':
            return random.random() * dmg * 2 + 5
        return random.random() * dmg + 1
        
    def has_sword(self):
        self.wapon = 'sword'
        
    def has_tool(self):
        self.tool = 'pickaxe'
        
    def has_treasure(self):
        self.treasure = 'amulet'
        
    def get_tool(self):
        if self.tool == 'pickaxe':
            return True
    def get_treasure(self):
        if self.treasure == 'amulet':
            return True
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player('{self.name}', '{self.loc}', '{self.hp}')"
