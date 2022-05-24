#!/usr/bin/env python3
import time
import mapping
import magic

import random
from gnome import Gnome
from human import Human
from items import Item
import player
import actions


ROWS = 25
COLUMNS = 80


if __name__ == "__main__":
    # initial parameters
    level = 0

    player = Human('Maxi', (random.randint(10,COLUMNS-10),random.randint(1,ROWS-1)),None)
    
    # initial locations may be random generated
    gnome = Gnome('Basic', (random.randint(10,COLUMNS-10), random.randint(1,ROWS-1)), None)

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

    turns = 0
    while dungeon.level >= 0:
        turns += 1
        # render map
        dungeon.render(player, gnome)
        # print(mapping.Level.are_connected((random.randint(0,COLUMNS), random.randint(0, ROWS)), (random.randint(0,COLUMNS), random.randint(0, ROWS))))
        # read key
        key = magic.read_single_keypress()
        
        # Hacer algo con keys:
        if key[-1] == 'w':  
            actions.move_up(dungeon, player)
        if key[-1] == 'd':
            actions.move_right(dungeon, player)
        if key[-1] == 's':
            actions.move_down(dungeon, player)
        if key[-1] == 'a':
            actions.move_left(dungeon, player)
        # if key[-1] == 'w' or key[-1] == 'd' or key[-1] == 's' or key[-1] == 'a':
        #     movement = [actions.move_up(dungeon, gnome),actions.move_right(dungeon, gnome), actions.move_down(dungeon, gnome), actions.move_left(dungeon, gnome)]
        #     random.choice(movement)
            

       
        # move player and/or gnomes

    # Salió del loop principal, termina el juego

 