import random
import items

class Player:
    def __init__(self, name, xy, face, hit_points=200):
        self.name = name
        self.x, self.y = xy
        self._hp = hit_points
        self.max_hp = hit_points
        self.alive = True
        self.face = face
    
    @property
    def hp(self):
        """
        The hp function returns the current hit points of the player and the max hit points.
        
        :param self: Reference the class instance itself
        :return: The value of the health attribute compared to the max health attribute as a string
        """
        return f'({self._hp}/{self.max_hp})'
    
    @property
    def location(self):
        """
        The location function returns the location of the object.
        
        :param self: Access variables that belongs to the class
        :return: A tuple of the x and y coordinates of the object
        """
        return f'({self.x}/{self.y})'
    
    def get_hp(self) -> int:
        """
        The get_hp function returns the current hit points of the player.
        
        :param self: Access the attributes and methods of the class
        :return: The value of the self._hp attribute
        """
        return self._hp
    
    def get_max_hp(self) -> int:
        """
        The get_max_hp function returns the maximum number of hit points that a player can have.
        
        :param self: Access the attributes and methods of the class
        :return: The maximum hit points of the character
        """
        return self.max_hp
    
    def get_alive(self):
        """
        The get_alive function returns a list of all the alive cells in the grid.
        
        :param self: Access variables that belongs to the class
        :return: Wethere the player is alive or not
        """
        return self.alive
    
    def set_hp(self, dmg):
        """
        The set_hp function takes a parameter dmg, which is an integer.
        It then subtracts the value of dmg from the current hp of the object.
        If this results in a number less than 1, it calls the kill() function.
        
        :param self: Refer to the object itself
        :param dmg: Subtract the damage from the hp
        :return: The new hp of the object
        """
        self._hp -= dmg
        if self._hp < 1:
            self.kill()

    def loc(self):
        """
        The loc function returns the coordinates of a given object in the.
        
        :param self: Reference the current instance of the class
        :return: x and y coordinates of the object
        """
        return self.x, self.y

    def move_to(self, xy):
        """
        The move_to function moves the object to a specified location.
        The function takes two arguments: x and y.
        The function moves the object to (x,y). 
        
        :param self: Access the attributes and methods of the class.
        :param xy: Specify the x and y coordinates of the object.
        :return: Sets the x and y coordinates of the object.
        """
        self.x, self.y = xy
        
    def kill(self):
        """
        The kill function sets the hp of the object to 0 and sets the alive value to False.
        
        :param self: Refer to the object class.
        :return: None.
        """
        self._hp = 0
        self.alive = False

        
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player('{self.name}', '({self.x,self.y})', '{self.hp}')"
