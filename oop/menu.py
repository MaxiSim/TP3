import random

import functions
from human import Human
from gnome import Gnome
import mapping
import game
from items import PickAxe


def rules():
    """
    The rules function prints out the rules of the game.
    """
    print('''
    The rules are simple:   
    -To move use w(up), a(left), s(down), d(right). 
    -To pick up items, just run over them. 
    -To attack enemies move onto them, and if you have a weapon('/'), you can deal extra damage.
    -To break down walls, just run over them while holding the pickaxe('7').
    -To use stairs(up'<' and down'>'), press "v" while standing on top, but remember to kill the gnome('G') first.
    -To win, you must grab the trasure('8') and escape the dungeon.''')
    call()
    
def play():
    funcplay = menu('Please select a gamemode or go back to the main menu.', list(funciones_menu_play.keys()))
    funciones_menu_play[funcplay]()
    
def customize():
    """
    The customize function allows the user to create a character. 
    It asks the user for input on what name and face they want their character to have. It also asks for the number of levels
    the player wnats for the dungeon.
    Then it creates a dungeon object, a human player object, a gnome plyaer object and an item(pickaxe) object.
    
    :return: calls the game_loop function to initialize the game.
    """

    name = input('Give your character a name: >')
    face = input('Choose a single charcter for your face: >')
    while face == '7' or face == '8' or face == '/' or face == 'G' or len(face) > 1:
        face = input('That is not a valid option. Try again: >')
    levels = input('''Choose a number of levels from 3 to 6: ''')
    while levels != '3' and levels != '4' and levels != '5' and levels != '6':
        levels = input('That is not a valid option. Try again: >')
    
    levels = int(levels)
    dungeon = mapping.Dungeon(25,80,levels)
    a,b = functions.check_path(dungeon)
    pickaxe = PickAxe('PickAxe','7')
    dungeon.add_item(pickaxe, 1, b)
    player = Human(name,a, None, face)
    gnome = Gnome('Gnome', (random.randint(0, 79), random.randint(0, 24)))
    
    return game.game_loop(dungeon, player, gnome, levels)

def standard():
    """
    The standard function creates a dungeon, a gnome, and then checks for a path between the player and the pickaxe.
    If there is one, it adds the player and pickaxe to those locations.
    
    :return: calls the game_loop function to initialize the game.
    """
    dungeon = mapping.Dungeon(25, 80)
    a,b = functions.check_path(dungeon)
    player = Human('Player', a, None)
    gnome = Gnome('Gnome', (random.randint(0, 79), random.randint(0, 24)))
    pickaxe = PickAxe('PickAxe','7')
    dungeon.add_item(pickaxe, 1, b)
    
    return game.game_loop(dungeon, player, gnome)


def menu(prompt: str, opciones: list) -> str :
      """
      The menu function displays a prompt and then displays a menu of options.
      It accepts the user's choice, validates it, and returns it. If the user enters
      an invalid option (not 1 or 2), then an error message is displayed and the menu
      is displayed again.
      
      :param prompt:str: Display a message to the user
      :param opciones:list: Pass a list of strings to the menu function
      :return: The selected function is returned
      """
      while True:   
         print(prompt)
         for i, opcion in enumerate(opciones):
            print(f'{i + 1}. {opcion}')
         selected = (input('> '))
         while selected != '1' and selected != '2' and selected != '3':
            selected = input('That is not a valid option. Try again: >')
         selected = int(selected)  
         return opciones[selected - 1]
        
def call():
      """
      The call function is the main function of the program. It is called by
      the main function and executes the menu function in this file. 
      Only when called by main.py, the file is executed.
      """
      func = menu('MENU', list(funciones_menu.keys()))
      funciones_menu[func]()
      
funciones_menu = {
    "See Rules": rules,
    "Play": play,
    "Quit": quit
}

funciones_menu_play = {
    "Play with custom character": customize,
    "Standard game": standard,
    "Go Back": call
}


    
      
