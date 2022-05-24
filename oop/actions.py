from typing import Union


import mapping
import player


numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def attack(dungeon, player, gnome):#completar
    # completar
    raise NotImplementedError


def move_to(dungeon: mapping.Dungeon, player: player.Player, location: tuple[numeric, numeric]):
    raise NotImplementedError
    
    
    


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
    raise NotImplementedError


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def pickup(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError
