import random
from typing import Optional

from sympy import Le
from human import Human

import player
import items


Location = tuple[int, int]


class Tile:
    """Tile(char: str, walkable: bool=True)

    A Tile is the object used to represent the type of the dungeon floor.

    Arguments

    char (str) -- string of length 1 that is rendered when rendering a map.
    walkable (bool) -- states if the tile is walkable or not.
    """
    def __init__(self, char: str, walkable: bool = True):
        self.walkable = walkable
        self.face = char

    def is_walkable(self) -> bool:
        """Returns True if the tile is walkable, False otherwise."""
        return self.walkable


AIR = Tile(' ')
WALL = Tile('▓', False)
STAIR_UP = Tile('<')
STAIR_DOWN = Tile('>')
LIMIT_V = Tile('|', False)
LIMIT_H = Tile('-', False)

class Level:
    """Level(rows: int, columns: int) -> Level

    Arguments

    rows (int) -- is the number of rows for the level.
    columns (int) -- is the number of columns for the level.

    Returns an instance of a level.
    """
    def __init__(self, rows: int, columns: int):
        """Initializes a dungeon level class. See class documentation."""
        tiles = [[1] * 12 + [0] * (columns - 24) + [1] * 12]  # 0=air 1=rocks
        for row in range(1, rows):
            local = tiles[row - 1][:]
            for i in range(2, columns - 2):
                vecindad = local[i - 1] + local[i] + local[i + 1]
                local[i] = random.choice([0]*100+[1]*(vecindad**3*40+1))
            tiles.append(local)

        for row in range(0, rows):
            for col in range(0, columns):
                tiles[row][col] = AIR if tiles[row][col] == 0 else WALL

        self.tiles = tiles
        self.rows, self.columns = rows, columns
        self.items = {}

    def find_free_tile(self) -> Location:
        """Randomly searches for a free location inside the level's map.
        This method might never end.
        """
        i, j = random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)
        while self.tiles[i][j] != AIR:
            i, j = random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)
        return (j, i)

    def get_random_location(self) -> Location:
        """Compute and return a random location in the map."""
        return random.randint(0, self.columns - 1), random.randint(0, self.rows - 1)

    def add_stair_up(self, location: Optional[Location] = None):
        """Add an ascending stair tile to a given or random location in the map."""
        if location is not None:
            j, i = location
        else:
            i = random.randint(0, self.rows - 1)
            j = random.randint(0, self.columns - 1)
        self.tiles[i][j] = STAIR_UP

    def add_stair_down(self, location: Optional[Location] = None):
        """Add a descending stair tile to a give or random location in the map."""
        if location is not None:
            j, i = location
        else:
            i = random.randint(0, self.rows - 1)
            j = random.randint(0, self.columns - 1)
        self.tiles[i][j] = STAIR_DOWN

    def add_item(self, item: items.Item, location: Optional[Location] = None):
        """Add an item to a given location in the map. If no location is given, one free space is randomly searched.
        This method might never if the probability of finding a free space is low.
        """
        if location is None:
            j, i = self.find_free_tile()
        else:
            j, i = location
        items = self.items.get((j, i), [])
        items.append(item)
        self.items[(j, i)] = items
        
        
        # gnome: player.Player

    def render(self, player: player.Player, gnome: player.Player, level: int):
        """Draw the map onto the terminal, including player and items. Player must have a loc() method, returning its
        location, and a face attribute. All items in the map must have a face attribute which is going to be shown. If
        there are multiple items in one location, only one will be rendered.
        """
        # completar (cuando se agregue el gnomo)
        print("-" + "-" * len(self.tiles[0]) + "-")
        for i, row in enumerate(self.tiles):
            print("|", end="")
            for j, cell in enumerate(row):
                if (j, i) == player.loc():
                    print(player.face, end='')
                elif (j,i) == gnome.loc():
                    print(gnome.face, end = '')
                elif (j, i) in self.items:
                    print(self.items[(j, i)][0].face, end='')
                else:
                    print(cell.face, end='')
            print("|")
        print("-" + "-" * len(self.tiles[0]) + "-")
        print(f'Player:{player}     HP:{player.hp}      Location:{player.location}      Level: {level}')

    def is_walkable(self, location: Location):
        """Check if a player can walk through a given location."""
        j, i = location
        return self.tiles[i % self.rows][j % self.columns].walkable

    def index(self, tile: Tile) -> Location:
        """Get the location of a given tile in the map. If there are multiple tiles of that type, then only one is
        returned.

        Arguments

        tile (Tile) -- one of the known tile types (AIR, WALL, STAIR_DOWN, STAIR_UP)

        Returns the location of that tile type or raises ValueError
        """
        for i in range(self.rows):
            try:
                j = self.tiles[i].index(tile)
                return j, i
            except ValueError:
                pass
        raise ValueError

    def loc(self, xy: Location) -> Tile:
        """Get the tile type at a give location."""
        j, i = xy
        return self.tiles[i][j]

    def get_items(self, xy: Location) -> list[items.Item]:
        """Get a list of all items at a given location. Removes the items from that location."""
        i, j = xy
        if (i, j) in self.items:
            items = self.items[(i, j)]
            del(self.items[(i, j)])
        else:
            items = []
        return items

    def dig(self, xy: Location) -> None:
        """Replace a WALL at the given location, by AIR."""
        j, i = xy
        if self.tiles[i][j] is WALL:
            self.tiles[i][j] = AIR

    def is_free(self, xy: Location) -> bool:
        """Check if a given location is free of other entities."""
        # completar
        raise NotImplementedError

    def are_connected(self, initial: Location, end: Location,  not_walkable : list = [], path_to: list = []) -> bool:
        """Check if there is walkable path between initial location and end location."""
        # if len(self.get_path(initial, end)) == 0:
        #     return False
       
        Up = (initial[0], initial[1]-1)
        Right = (initial[0]+1, initial[1])
        Down = (initial[0], initial[1]+1)
        Left = (initial[0]-1, initial[1])

        # d = [Up, Right, Down, Left]
        # result = False

        # for direction in d:
        #     if self.is_walkable(direction):
        #         if direction not in not_walkable:
        #             t = self.are_connected(direction, end, not_walkable + initial , path_to + initial)
        #             if t:
        #                 return True 
        # return result
      
        if initial == end:
                    path_to.append(end)
                    return True
        
        else:
            if self.is_walkable(Up) == True and Up not in path_to and Up not in not_walkable:
                path_to.append(initial)
                return self.are_connected(Up, end, not_walkable, path_to)
            elif self.is_walkable(Right) == True and Right not in path_to and Right not in not_walkable:
                path_to.append(initial)
                return self.are_connected(Right, end, not_walkable, path_to)
            elif self.is_walkable(Down) == True and Down not in path_to and Down not in not_walkable:
                path_to.append(initial)
                return self.are_connected(Down, end, not_walkable, path_to)
            elif self.is_walkable(Left) == True and Left not in path_to and Left not in not_walkable:
                path_to.append(initial)
                return self.are_connected(Left, end, not_walkable, path_to)
            elif (not self.is_walkable(Up) or Up in not_walkable)and (not self.is_walkable(Right) or Right in not_walkable) and (not self.is_walkable(Down) or Down in not_walkable) and (not self.is_walkable(Left) or Left in not_walkable):
                if len(path_to) == 0:
                    return False
                else:
                    not_walkable.append(initial)
                    return self.are_connected(path_to[0], end, not_walkable, path_to = [])

    def get_path(self, initial: Location, end: Location) -> list:
        """Return a sequence of locations between initial location and end location, if it exits."""
        pass
        

class Dungeon:
    """Dungeon(rows: int, columns: int, levels: int = 3) -> Dungeon

    Arguments

    rows (int) -- is the number of rows for the dungeon.
    columns (int) -- is the number of columns for the dungeon.
    levels (int) -- is the number of levels for the dungeon (default: 3).

    Returns an instance of a dungeon.
    """
    def __init__(self, rows: int, columns: int, levels: int = 3):
        """Initializes a dungeon class. See class documentation."""
        self.dungeon = [Level(rows, columns) for _ in range(levels)]
        self.rows = rows
        self.columns = columns
        self.level = 0

        self.stairs_up = [level.get_random_location() for level in self.dungeon]
        self.stairs_down = [level.get_random_location() for level in self.dungeon[:-1]]

        for level, loc_up, loc_down in zip(self.dungeon[:-1], self.stairs_up[:-1], self.stairs_down):
            # Ubicar escalera que sube
            level.add_stair_up(loc_up)

            # Ubicar escalera que baja
            level.add_stair_down(loc_down)

        # Ubicar escalera del nivel inferior
        self.dungeon[-1].add_stair_up(self.stairs_up[-1])

    def render(self, player: player.Player, gnome:player.Player):
        """Draw current level onto the terminal, including player and items. Player must have a loc() method, returning
        its location, and a face attribute. All items in the map must have a face attribute which is going to be shown.
        If there are multiple items in one location, only one will be rendered.
        """
        self.dungeon[self.level].render(player, gnome, self.level)

    def find_free_tile(self) -> Location:
        """Randomly searches for a free location inside the level's map.
        This method might never end.
        """
        return self.dungeon[self.level].find_free_tile()

    def is_walkable(self, tile: Tile):
        """Check if a player can walk through a given location. See Level.is_walkable()."""
        return self.dungeon[self.level].is_walkable(tile)

    def add_item(self, item: items.Item, level: Optional[int] = None, xy: Optional[Location] = None):
        """Add an item to a given location in the map of a given or current level. If no location is given, one free
        space is randomly searched. This method might never if the probability of finding a free space is low.
        """
        if level is None:
            level = self.level + 1
        if 0 < level <= len(self.dungeon):
            self.dungeon[level - 1].add_item(item, xy)

    def loc(self, xy: Location) -> Tile:
        """Get the tile type at a give location."""
        return self.dungeon[self.level].loc(xy)

    def index(self, tile: Tile) -> Location:
        """Get the location of a given tile in the map. If there are multiple tiles of that type, then only one is
        returned. See Level.index().
        """
        return self.dungeon[self.level].index(tile)

    def get_items(self, xy: Location) -> list[items.Item]:
        """Get a list of all items at a given location. Removes the items from that location. See Level.get_items()."""
        return self.dungeon[self.level].get_items(xy)

    def dig(self, xy: Location) -> None:
        """Replace a WALL at the given location, by AIR. See Level.dig()."""
        return self.dungeon[self.level].dig(xy)

    def is_free(self, xy: Location) -> bool:
        """NOT IMPLEMENTED. Check if a given location is free of other entities. See Level.is_free()."""
        return self.dungeon[self.level].is_free(xy)

    def set_level(self, value):
        if value == 1:
            self.level += 1
        elif value == 0:
            self.level -= 1
    
    def get_level(self):
        return self.level
    
    def are_connected(self, initial: Location, end: Location) -> bool:
        """Check if two locations are connected. See Level.are_connected()."""
        return self.dungeon[self.level].are_connected(initial, end)
    