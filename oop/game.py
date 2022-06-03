#!/usr/bin/env python3
import time
import mapping
import magic

import items
import player
import actions
import menu


ROWS = 25
COLUMNS = 80


def game_loop(dungeon: mapping.Dungeon, player: player.Player, gnome: player.Player, levels: int = 3):
        """
        The game_loop function is the main function of the game. It is responsible for
        the main loop of the game, which includes rendering the map, reading user input and
        doing all other necessary actions. The function also checks if player can get out 
        of dungeon or not.
        
        :param dungeon:mapping.Dungeon: Check the player's position in the dungeon
        :param player:player.Player: Human player object
        :param gnome:player.Player: Gnome player object
        :param levels:int=3: Default number of levels in the dungeon
        """
        # create fixed items
        sword = items.Sword('Sword','∫',5,10)
        amulet = items.Amulet('Amulet','◊')
        
        # add fixed items to the dungeon
        dungeon.add_item(sword, 2)
        dungeon.add_item(amulet, levels)

        
        # main game development
        turns = 0
        regen = 0
        while dungeon.level >= 0 and player.get_hp() > 0:
            turns += 1
            # render map
            print('You were teleported into the dungeon. Try to escape!')
            dungeon.render(player, gnome)
            # read key
            key = magic.read_single_keypress()
            # move player and/or gnomes
            actions.move_to(dungeon, player, key, gnome)
            actions.move_gnome(dungeon, gnome)
            # pick up items
            actions.pickup(dungeon, player)
            # attack and regenerate
            actions.attack(player, gnome)
            regen = actions.regenerate(player, gnome, regen)
        
        # checks if player can get out of the dungeon or not
        if dungeon.level == -1 and type(player.get_treasure()) == items.Amulet:
            print('You win!')
        else:
            if dungeon.level == -1:
                print('You were killed by lightning!')
            elif player.get_hp() <= 0:
                print('You died! Get stronger for next time!')
            print('GAME OVER')
            print('')
        
        menu.call()
        # Out of principal loop, game ends

    