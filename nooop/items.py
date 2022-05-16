import config


def create_sword(name, location):
    return {
        "name": name,
        "location": location,
        "face": config.SWORD,
        "type": "weapon"
    }


def create_pickaxe(name, location):
    return {
        "name": name,
        "location": location,
        "face": config.PICK,
        "type": "tool"
    }


def create_amulet(name, location):
    return {
        "name": name,
        "location": location,
        "face": config.TREASURE,
        "type": "treasure"
    }
