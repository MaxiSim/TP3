import player
import mapping 


def check_path(initial: tuple, end: tuple):
    if mapping.are_connected(initial, end) == True:
        return True
    elif mapping.are_connected(initial, end) == False:
        return 
    
        
    
    
    