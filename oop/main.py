from player import Player

if __name__ == '__main__':
    xy = [0,0]
    player = Player('maxi',xy)
    # Recibe el evento del teclado y mueve al player
    # Moverse
    xy[0] += 1
    xy[1] += 1
    
    player.move_to(xy)
    
    print(player.loc())