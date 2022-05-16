from typing import List, Tuple

import config
import human


def move(level: List[List[int]],
         character: dict,
         direction: str):
    """
    Moves an entity from a given location to the appropriate location based on the game level and equipment for the
    character.

    :param level: Game floor in which the character is moving.
    :param character: Dictionary representing the character.
    :param direction: UP, DOWN, LEFT or RIGHT command (configured in characters.py)

    :return: Tuple with coordinates where the character would move in the given direction
    without accounting enemies or hazards.
    Still, moving towards walls make characters without a PICK stand and not move.
    """
    # completar
    raise NotImplementedError


def move_to(level: List[List[int]], entity: dict, location: Tuple[int, int]):
    # completar
    raise NotImplementedError


def move_up(level: List[List[int]], entity: dict):
    # completar
    raise NotImplementedError


def move_left(level: List[List[int]], entity: dict):
    # completar
    raise NotImplementedError


def move_down(level: List[List[int]], entity: dict):
    # completar
    raise NotImplementedError


def move_right(level: List[List[int]], entity: dict):
    # completar
    raise NotImplementedError
