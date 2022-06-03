import random
from player import Player

class Gnome(Player):
    def __init__(self, name, xy, face = 'G', hit_points = 100):
        super().__init__(name, xy, face, hit_points = hit_points)
        
    
    def damage(self, dmg = 10):
        """
        The damage function takes the amount of damage done by the gnome.
        If the gnome is dead, then it does not make any damage.
        
        :param self: Access variables that belongs to the class
        :param dmg=10: Determine the base damage of the attack
        :return: A random number between 1 and 5 times the damage
        """
        if self.alive == True:
            return random.randint(1,5)*dmg
        else:
            return 0
        
    def respawn(self):
        """
        The respawn function takes the current hp of the character and sets it to its max hp.
        It also sets the alive attribute to True.
        
        :param self: Refer to the object itself
        :return: The value of the object's hp attribute and the value of the object's alive attribute
        """
        self._hp = self.max_hp
        self.alive = True
    
    