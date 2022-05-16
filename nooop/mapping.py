import random
from typing import List, Tuple


import config


def render(tiles: List[List[int]],
           player: dict, gnome: dict):
    """
    Draw the map onto the terminal, including player, items and gnome.

    :param tiles: dungeon level, created with level(). Is a list of lists of ints.
    :param player: player location in the map (dict).
    :param gnome: gnome location in the map (dict).

    :return: None, map is rendered on screen.
    """
    print("-" + "-" * len(tiles[0]) + "-")
    for i, row in enumerate(tiles):
        print("|", end="")
        for j, cell in enumerate(row):
            if (i, j) == player["location"]:
                print(player["face"], end='')
            elif gnome and (i, j) == gnome["location"]:
                print(gnome["face"], end='')
            elif cell == 0:
                print(config.SPACE, end='')
            elif cell == 1:
                print(config.WALL_ROCK, end='')
            else:
                print(cell, end='')
        print("|")
    print("-" + "-" * len(tiles[0]) + "-")


def level(rows: int,
          columns: int) -> List[List[int]]:
    """
    Creates a dungeon level

    :param rows: is the number of rows for the level (int).
    :param columns: is the number of columns for the level (int).

    :return: level map
    """
    tiles = [[1] * 12 + [0] * (columns - 24) + [1] * 12]  # 0=air 1=rocks
    for row in range(1, rows):
        local = tiles[row - 1][:]
        for i in range(2, columns - 2):
            vecindad = local[i - 1] + local[i] + local[i + 1]
            local[i] = random.choice([0]*100+[1]*(vecindad**3*40+1))
        tiles.append(local)

    return tiles


def dungeon(rows: int,
            columns: int,
            levels: int = 3) -> List[List[List[int]]]:
    """
    Creates a dungeon

    :param rows: is the number of rows for each level (int).
    :param columns: is the number of columns for each level (int).
    :param levels: the number of levels that the dungeon should have (int).

    :return: dungeon
    """
    dungeon_levels = [level(rows, columns) for _ in range(levels)]

    up = []
    down = []
    for i in range(levels - 1):
        # Up stairs
        x = random.randint(0, rows - 1)
        y = random.randint(0, columns - 1)
        up.append((x, y))
        dungeon_levels[i][x][y] = config.LADDER_UP

        # Down stairs
        x = random.randint(0, rows - 1)
        y = random.randint(0, columns - 1)
        down.append((x, y))
        dungeon_levels[i][x][y] = config.LADDER_DOWN

    # Last Up stair
    x = random.randint(0, rows - 1)
    y = random.randint(0, columns - 1)
    up.append((x, y))
    dungeon_levels[-1][x][y] = config.LADDER_UP

    return dungeon_levels


def add_item(dungeon: List[List[List[int]]],
             item: dict,
             level: int):
    """
    Places items on a newly generated map. Unreachability of positions is not checked by the function.

    :param dungeon: dungeon to be modified.
    :param item: item to add
    :param level: floor number

    :return: No return value, map is modified in-place.
    """
    x, y = item["location"]
    dungeon[level][x][y] = item["face"]


def is_tile(level: List[List[int]],
            location: Tuple[int, int],
            tile: str) -> bool:
    """
    Checks if a given location of the level map is of a give tile type, por example, a stair up '<'.

    :param level: dungeon level map (list of lists of ints)
    :param location: coordinates of the tile to check (tuple of ints)
    :param tile: type of tile to see (all tiles are 1 character---strings of lenth 1)

    :return: True if it is, False otherwise.
    """
    x, y = location
    return level[x][y] == tile


def set_tile(level: List[List[int]],
             location: Tuple[int, int],
             tile: str):
    """
    Set a given location of a level map with the specified tile.

    :param level: dungeon level map (list of lists of ints)
    :param location: coordinates of the tile to check (tuple of ints)
    :param tile: type of tile to see (all tiles are 1 character---strings of lenth 1)

    :return: No return value, map is modified in-place.
    """
    x, y = location
    level[x][y] = tile


def is_free(level: List[List[int]],
            xy: Tuple[int, int]) -> bool:
    """Check if a given location is free of other entities."""
    # completar
    raise NotImplementedError


def are_connected(level: List[List[int]],
                  initial: Tuple[int, int],
                  end: Tuple[int, int]) -> bool:
    """Check if there is walkable path between initial location and end location."""
    # completar
    raise NotImplementedError


def get_path(level: List[List[int]],
             initial: Tuple[int, int],
             end: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Return a sequence of locations between initial location and end location, if it exits."""
    # completar
    raise NotImplementedError
