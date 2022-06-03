import mapping
import sys
sys.setrecursionlimit(10000)

def check_path(dungeon: mapping.Dungeon):
    """
    The check_path function checks that two locations are connected.
    
    :param dungeon:mapping.Dungeon: Access the dungeon's map
    :return: a and b, two connected coordinates in the dungeon.
    """
    a = dungeon.find_free_tile()
    b = dungeon.find_free_tile()
    not_walkable = []
    path_to = []
    result = dungeon.are_connected(a,b, not_walkable, path_to)
    while result != "Path found" :
        not_walkable.clear()
        path_to.clear()
        a = dungeon.find_free_tile()
        b = dungeon.find_free_tile()
        
    return a,b
    
        
    
    
    