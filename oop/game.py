#!/usr/bin/env python3
import time
import mapping
import magic

import random
from human import Human
from items import Item
import actions


ROWS = 25
COLUMNS = 80


if __name__ == "__main__":
    # initial parameters
    level = 0
    player =

    # initial locations may be random generated
    gnomes =

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

    turns = 0
    while dungeon.level >= 0:
        turns += 1
        # render map
        dungeon.render()

        # read key
        key = magic.read_single_keypress()

        # Hacer algo con keys:
        # move player and/or gnomes

    # Salió del loop principal, termina el juego
