#!/usr/bin/env python3
import time
import mapping
import magic


import random
from functions import check_path
from gnome import Gnome
from human import Human
from items import PickAxe, Sword, Amulet
import player
import actions


ROWS = 25
COLUMNS = 80




if __name__ == "__main__":
        # initial parameters
        level = 0
        # initial locations may be random generated
        player = Human('Maxi',(random.randint(0, COLUMNS-1), random.randint(0, ROWS-1)),None)
        gnome = Gnome('Basic', (random.randint(0,COLUMNS-1), random.randint(0,ROWS-1)), None)
        pickaxe = PickAxe('PickAxe','7')
        sword = Sword('Sword','/',5,10)
        amulet = Amulet('Amulet','8')

        dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
        dungeon.add_item(pickaxe)
        dungeon.add_item(sword, 2)
        dungeon.add_item(amulet)
        
        check_path(dungeon,(random.randint(0,COLUMNS-1), random.randint(0,ROWS-1)) ,(random.randint(0,COLUMNS-1), random.randint(0,ROWS-1)) )
            
        # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

        turns = 0
        while dungeon.level >= 0:
            turns += 1
            # render map
            dungeon.render(player, gnome)
            
            # read key
            key = magic.read_single_keypress()
            

            # move player and/or gnomes
            if key[-1] == 'w':  
                actions.move_up(dungeon, player)
            if key[-1] == 'd': 
                actions.move_right(dungeon, player)
            if key[-1] == 's':
                actions.move_down(dungeon, player)
            if key[-1] == 'a':
                actions.move_left(dungeon, player)
            actions.move_gnome(dungeon, player, gnome)
            
            # Hacer algo con keys:
            if key[-1] == 'v':
                if dungeon.loc(player.loc()) == mapping.STAIR_DOWN:
                    actions.descend_stair(dungeon,player)
                elif dungeon.loc(player.loc()) == mapping.STAIR_UP:
                    actions.climb_stair(dungeon, player)
            
            actions.pickup(dungeon, player)
        
            
        
            # print(type(dungeon.get_items((50,20))[0]))
            
        if dungeon.level == -1 and type(player.get_treasure() == Amulet):
            print('You win!')
        else:
            print('You were killed by lightning!')
            print('GAME OVER')
            
        
            


        # Salió del loop principal, termina el juego

    