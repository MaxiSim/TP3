from typing import Union
import random

import mapping
import player


numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

def move_gnome(dungeon, player, gnome):
    direction = random.randint(1,5)
    if direction == 1:
        return move_up(dungeon, gnome)
    elif direction == 2:
        return move_right(dungeon, gnome)
    elif direction == 3:
        return move_down(dungeon, gnome)
    elif direction == 4:
        return move_left(dungeon, gnome)
    elif direction == 5:
        return None

def attack(dungeon, player, gnome):#completar
    # completar
    raise NotImplementedError


def move_to(dungeon: mapping.Dungeon, player: player.Player, location: tuple[numeric, numeric]):
    return player.move_to(location)
    
    
    


def move_up(dungeon: mapping.Dungeon, player: player.Player):
    playerloc = player.loc()
    xy = (playerloc[0], playerloc[1]-1)
    if dungeon.is_walkable(xy) == True and xy[1]>=0:
        return player.move_to(xy)
    else:
        return player.move_to(player.loc())


def move_down(dungeon: mapping.Dungeon, player: player.Player):
    playerloc = player.loc()
    xy = (playerloc[0], playerloc[1]+1)
    if dungeon.is_walkable(xy) == True and xy[1]<=24:
        return player.move_to(xy)
    else:
        return player.move_to(player.loc())
    


def move_left(dungeon: mapping.Dungeon, player: player.Player):
    playerloc = player.loc()
    xy = (playerloc[0]-1, playerloc[1])
    if dungeon.is_walkable(xy) == True and xy[0]>=0:
        return player.move_to(xy)
    else:
        return player.move_to(player.loc())


def move_right(dungeon: mapping.Dungeon, player: player.Player):
    playerloc = player.loc()
    xy = (playerloc[0]+1, playerloc[1])
    if dungeon.is_walkable(xy) == True and xy[0]<= 79:
        return player.move_to(xy)
    else:
        return player.move_to(player.loc())


def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    # raise NotImplementedError
    if player.loc() == dungeon.index(mapping.STAIR_UP) and dungeon.level != 0:
        return dungeon.set_level(0), move_to(dungeon, player, dungeon.index(mapping.STAIR_DOWN))
    else:
        return dungeon.set_level(0)


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    # raise NotImplementedError
    if player.loc() == dungeon.index(mapping.STAIR_DOWN):
        return dungeon.set_level(1), move_to(dungeon,player,dungeon.index(mapping.STAIR_UP))
    


def pickup(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError
