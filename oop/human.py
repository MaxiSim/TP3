import random
from player import Player
import items

class Human(Player):
    def __init__(self, name, xy, weapon = None, face = '@', hit_points = 200, tool = None, treasure = None):
        super().__init__(name, xy, face, hit_points = hit_points)
        self.tool = tool
        self.treasure = treasure
        self.weapon = weapon
        self.inventory =[]
        
    def set_hp_recovery(self, value: int):
        """
        The set_hp_recovery function sets the hp of the character to a value that is less than or equal to max_hp.
        If the value passed in is greater than max_hp, then it sets hp to be equal to max_hp.
        
        :param self: Access the attributes and methods of the class
        :param value:int: Add 30hp to the current hp of the character
        :return: Nothing
        """
        if self._hp + value > self.max_hp:
            self._hp = self.max_hp
        else:
            self._hp += value
        
    def has_sword(self, sword):
        """
        The has_sword function takes a sword as an argument and sets the weapon attribute to that sword.
        
        :param self: Refer to the object of the class
        :param sword: Set the weapon attribute of the player to a sword
        :return: The weapon attribute of the player
        """
        self.weapon = sword[0] 
        self.inventory.append('Sword')
           
    def has_tool(self, tool):
        """
        The has_tool function takes a tool as an argument and sets the tool attribute to that tool.
        
        :param self: Access the attributes and methods of the class
        :param tool: Set the tool attribute of the player to a tool
        :return: The tool attribute of the player
        """
        self.tool = tool[0]
        self.inventory.append('PickAxe')
        
    def has_treasure(self, treasure):
        """
        The has_treasure function takes a treasure as an argument and sets the treasure attribute to that treasure.
        
        :param self: Access the attributes and methods of the class
        :param tool: Set the treasure attribute of the player to a treasure
        :return: The treasure attribute of the player
        """
        self.treasure = treasure[0]
        self.inventory.append('Amulet')
        
    def get_tool(self):
        """
        The get_tool function returns the tool object.

        :param self: Access variables and methods of the objects class
        :return: The tool object
        """
        return self.tool
    
    def get_treasure(self):
        """
        The get_treasure function returns the treasure object.

        :param self: Access variables and methods of the objects class
        :return: The treasure object
        """
        return self.treasure

    def get_weapon(self):
        """
        The get_weapon function returns the weapon object.

        :param self: Access variables and methods of the objects class
        :return: The weapon object
        """
        return self.weapon

    def damage(self, dmg = 20):   
        """
        The damage function takes the default damage value of the player.
        If the player has a weapon equipped, then the damage is multiplied by the damage multiplier of the weapon.
        If there is no weapon equipped, then a default damage is returned.
        
        :param self: Refer to the object itself
        :param dmg=20: Determine default damage value
        :return: A value of how much damage the player will do
        """
        if type(self.get_weapon()) == items.Sword:
            return random.randint(1,2) * dmg * 2
        return dmg
    
    def get_inventory(self):
        """
        The get_inventory function returns a list of all the items in the inventory.
        
        :param self: Access variables that belongs to the class
        :return: A list of all the items in the player's inventory
        """
        return self.inventory


