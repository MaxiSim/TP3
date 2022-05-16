import human
import items
import actions

import mapping
import config
from getch import getch
import random as rnd


if __name__ == '__main__':
    # initial parameters
    level = 0
    player =

    # initial locations may be random generated
    gnomes =

    dungeon = mapping.dungeon(config.ROWS, config.COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

    # game loop
    key = None
    turns = 0
    while cmd != config.EXIT and level >= 0:
        turns += 1
        # render map
        mapping.render()

        # read key
        key = getch()

        # Hacer algo con keys:
        # move player and/or gnomes

    # Salió del loop principal, termina el juego
