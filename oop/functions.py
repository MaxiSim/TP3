import player
import mapping
import random
# from game import ROWS, COLUMNS

# def get_spawn(columns, rows)-> tuple:
    # xy = (random.randint(0,columns), random.randint(0,rows))
    # return xy

def check_path(dungeon: mapping.Dungeon, initial: tuple, end: tuple):
    if dungeon.are_connected(initial, end) == True:
        print('entra')
        # player.move_to(initial)
        # dungeon.add_item(pickaxe,0, end)
        
    elif dungeon.are_connected(initial, end) == False:
        # return 
        print('entra en false')
        # check_path(dungeon, (random.randint(0,COLUMNS-1), random.randint(0,ROWS-1)), (random.randint(0,COLUMNS-1), random.randint(0,ROWS-1)))
        
    else:
        print('no entra')
    
        
    
    
    