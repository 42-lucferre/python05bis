from ..elements import create_air
import elements
from .. import potions


def lead_to_gold() -> str:
    return f"Recipe transmuting Lead to Gold: brew '{create_air()}' and " \
           f"'{potions.strength_potion()}' mixed with " \
           f"'{elements.create_fire()}'"
