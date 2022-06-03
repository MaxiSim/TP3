from typing import Union
import random

import items
import gnome
import human
import mapping
import player


numeric = Union[int, float]



def move_gnome(dungeon, gnome: gnome.Gnome):
    """
    The move_gnome function moves the gnome around the dungeon. It takes two arguments:
    the dungeon map and a gnome object. The function returns nothing.
    
    :param dungeon: Check if the new location is walkable
    :param gnome:gnome.Gnome: Access the gnome's location
    :return: The new location of the gnome
    """
    direction = random.randint(1,10)
    gnome_loc = gnome.loc()
    Up = (gnome_loc[0], gnome_loc[1]-1)
    Right = (gnome_loc[0]+1, gnome_loc[1])
    Down = (gnome_loc[0], gnome_loc[1]+1)
    Left = (gnome_loc[0]-1, gnome_loc[1])
    
    if (direction == 1 or direction == 6) and dungeon.is_walkable(Up) == True and Up[1]>=0:
        return gnome.move_to(Up)
    elif (direction == 2 or direction == 7) and dungeon.is_walkable(Right) == True and Right[0]<=79:
        return gnome.move_to(Right)
    elif (direction == 3 or direction == 8) and dungeon.is_walkable(Down) == True and Down[1]<=24:
        return gnome.move_to(Down)
    elif (direction == 4 or direction == 9) and dungeon.is_walkable(Left) == True and Left[0]>=0:
        return gnome.move_to(Left)
    elif (direction == 5 or direction == 10):
        return None
    
def regenerate(player: human.Human, gnome: gnome.Gnome, regen):
    """
    The regenerate function is used to heal the player if they are not at full health and have killed a gnome.
    The function takes in two parameters, the player object and a boolean value that is true if the player has killed
    a gnome. If this boolean value is true then it will add 30 points to their current hp.
    
    :param player:human.Human: used to access the players current hp and max hp.
    :param gnome:gnome.Gnome: Check if the gnome is alive.
    :param regen: Determine whether the player is regenerating or not.
    :return: 1 if the player is alive, has killed the gnome and has less than max hp.
    """
    if gnome.get_alive() == False and player.get_hp() < player.get_max_hp() and regen == 0:
        player.set_hp_recovery(30)
        return 1
    elif gnome.get_alive() == True:
        return 0

def attack(player: human.Human, gnome: gnome.Gnome):
    """
    The attack function takes two arguments, player and gnome.
    If the player is in the same location as a gnome, then it will randomly choose an integer between 1 and 7.
    If that number is 1 or 2 or 3 or 7, the player will attack the gnome.
    If the number is 4 or 5, the gnome will attack the player.
    If the number is 6, both the player and the gnome will attack each other.
    
    :param player:human.Human: Access the player's location, hp, and damage.
    :param gnome:gnome.Gnome: Access the gnome's location, hp, and damage.
    :return: Deals damage to the gnome. Deals damage to the player. Deals damage to both the player and the gnome.
    """
    if player.loc() == gnome.loc():
        attacker = random.randint(1,7)
        if attacker == 1 or attacker == 2 or attacker == 3 or attacker == 7:
            # Player attacks gnome
            return gnome.set_hp(player.damage())
        elif attacker == 4 or attacker == 5:
            # Gnome attacks player
            return player.set_hp(gnome.damage())
        elif attacker == 6:
            # Both recieve damage
            return player.set_hp(gnome.damage()), gnome.set_hp(player.damage())


def move_to(dungeon: mapping.Dungeon, player: player.Player, key: tuple, gnome: gnome.Gnome):
    """
    The move_to function takes a dungeon, player, and gnome as arguments.
    It then checks to see if the key is w, d, s, a or v. If it is one of those keys
    then the function will call move_up(), move_right(), move_down(), 
    move_left() or descend_stair() and climb_stair() respectively.
    
    :param dungeon:mapping.Dungeon: Get the current level of the dungeon.
    :param player:player.Player: Access the player's location.
    :param key:tuple: Determine which direction the player is moving.
    :param gnome:gnome.Gnome: Pass the gnome object between functions.
    :return: None
    """
    if key[-1] == 'w':  
        move_up(dungeon, player)
    if key[-1] == 'd': 
        move_right(dungeon, player)
    if key[-1] == 's':
        move_down(dungeon, player)
    if key[-1] == 'a':
        move_left(dungeon, player)
    
    if key[-1] == 'v':
        if dungeon.loc(player.loc()) == mapping.STAIR_DOWN:
            descend_stair(dungeon,player, gnome)
        elif dungeon.loc(player.loc()) == mapping.STAIR_UP:
            climb_stair(dungeon, player, gnome)
    

def move_up(dungeon: mapping.Dungeon, player: human.Human):
    """
    The move_up function moves the player up one space in the dungeon.
    It takes two arguments: a Dungeon object and a Human object.
    If there is no wall at that location, it moves the player to that location.
    
    :param dungeon:mapping.Dungeon: Access the dungeons map.
    :param player:human.Human: Access the player's location.
    :return: Moves the player to the new location.
    """
    playerloc = player.loc()
    xy = (playerloc[0], playerloc[1]-1)
    if (dungeon.is_walkable(xy) == True or type(player.get_tool()) == items.PickAxe)and xy[1]>=0:
        dungeon.dig(xy)
        return player.move_to(xy)
    return player.move_to(player.loc())


def move_down(dungeon: mapping.Dungeon, player: human.Human):
    """
    The move_up function moves the player down one space in the dungeon.
    It takes two arguments: a Dungeon object and a Human object.
    If there is no wall at that location, it moves the player to that location.
    
    :param dungeon:mapping.Dungeon: Access the dungeons map.
    :param player:human.Human: Access the player's location.
    :return: Moves the player to the new location.
    """
    playerloc = player.loc()
    xy = (playerloc[0], playerloc[1]+1)
    if (dungeon.is_walkable(xy) == True or type(player.get_tool()) == items.PickAxe) and xy[1]<=24:
        dungeon.dig(xy)
        return player.move_to(xy)
    return player.move_to(player.loc())
    


def move_left(dungeon: mapping.Dungeon, player: human.Human):
    """
    The move_up function moves the player one space to the left in the dungeon.
    It takes two arguments: a Dungeon object and a Human object.
    If there is no wall at that location, it moves the player to that location.
    
    :param dungeon:mapping.Dungeon: Access the dungeons map.
    :param player:human.Human: Access the player's location.
    :return: Moves the player to the new location.
    """
    playerloc = player.loc()
    xy = (playerloc[0]-1, playerloc[1])
    if (dungeon.is_walkable(xy) == True or type(player.get_tool()) == items.PickAxe)and xy[0]>=0:
        dungeon.dig(xy)
        return player.move_to(xy)
    return player.move_to(player.loc())


def move_right(dungeon: mapping.Dungeon, player: human.Human):
    """
    The move_up function moves the player one space to the right in the dungeon.
    It takes two arguments: a Dungeon object and a Human object.
    If there is no wall at that location, it moves the player to that location.
    
    :param dungeon:mapping.Dungeon: Access the dungeons map.
    :param player:human.Human: Access the player's location.
    :return: Moves the player to the new location.
    """
    playerloc = player.loc()
    xy = (playerloc[0]+1, playerloc[1])
    if (dungeon.is_walkable(xy) == True or type(player.get_tool()) == items.PickAxe)  and xy[0]<= 79:
        dungeon.dig(xy)
        return player.move_to(xy)
    return player.move_to(player.loc())


def climb_stair(dungeon: mapping.Dungeon, player: player.Player, gnome: gnome.Gnome):
    """
    The climb_stair function handles the logic for climbing stairs.
    It takes a dungeon, player, and gnome as arguments. If the player is on a stair
    up tile and the dungeon level is not 0, it returns an upper level of the dungeon.
    
    :param dungeon:mapping.Dungeon: Access the current level of the dungeon.
    :param player:player.Player: Check if the player is on the stair up tile.
    :param gnome:gnome.Gnome: Used to kill the gnome when the player goes back to a previuos floor.
    :return: A previuos level dungeon, a player at the stair down location and a gnome that is dead
    """
    if player.loc() == dungeon.index(mapping.STAIR_UP) and dungeon.level != 0:
        return dungeon.set_level(0), player.move_to(dungeon.index(mapping.STAIR_DOWN)), gnome.kill()
    else:
        return dungeon.set_level(0)


def descend_stair(dungeon: mapping.Dungeon, player: player.Player, gnome: gnome.Gnome):
    """
    The descend_stair function handles the logic for going down stairs.
    It takes a dungeon, player, and gnome as arguments. If the player is on a stair
    down tile and the gnome is dead, it returns a lower level of the dungeon.
    
    :param dungeon:mapping.Dungeon: Access the current level of the dungeon.
    :param player:player.Player: Check if the player is on the stair up tile.
    :param gnome:gnome.Gnome: Used check if the gnome is dead or alive.
    :return: Next level of the dungeon, a player at the stair up location and respawn the gnome.
    """
    if player.loc() == dungeon.index(mapping.STAIR_DOWN) and gnome.get_alive() == False:
        return dungeon.set_level(1), player.move_to(dungeon.index(mapping.STAIR_UP)), gnome.respawn()
    else:
        print('You must kill the gnome to get the key!')
    
    
def pickup(dungeon: mapping.Dungeon, player: human.Human):
    """
    The pickup function allows the player to pick up items.
    
    :param dungeon:mapping.Dungeon: Get the items at the player's current location.
    :param player:human.Human: Access the player's location and methods.
    :return: adds the item to the player's inventory and deletes it from the dungeon.
    """
    element = dungeon.get_items(player.loc())
    if len(element) != 0:
        if type(element[0]) == items.Amulet:
            player.has_treasure(element)
        elif type(element[0]) == items.PickAxe:
            player.has_tool(element)
        elif type(element[0]) == items.Sword:
            player.has_sword(element)