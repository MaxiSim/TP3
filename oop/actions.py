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
    # completar
    raise NotImplementedError


def move_up(dungeon: mapping.Dungeon, player: player.Player):
    playerloc = player.loc()
    xy = (playerloc[0], playerloc[1]-1)
    return player.move_to(xy)


def move_down(dungeon: mapping.Dungeon, player: player.Player):
    playerloc = player.loc()
    xy = (playerloc[0], playerloc[1]+1)
    return player.move_to(xy)
    


def move_left(dungeon: mapping.Dungeon, player: player.Player):
    playerloc = player.loc()
    xy = (playerloc[0]-1, playerloc[1])
    return player.move_to(xy)


def move_right(dungeon: mapping.Dungeon, player: player.Player):
    playerloc = player.loc()
    xy = (playerloc[0]+1, playerloc[1])
    return player.move_to(xy)


def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def pickup(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError
