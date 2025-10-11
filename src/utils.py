from dataclasses import dataclass
from typing import List, Tuple, Optional



GRID_SIZE = 13

EMPTY = '.'
DANGER = 'P'
FRODO = 'F'
GOLLUM = 'G'
MOUNT_DOOM = 'M'
MITHRIL = 'C'
ORC = 'O'
URUK = 'U'
NAZGUL = 'N'
WATCHTOWER = 'W'

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # NESW



@dataclass(frozen=True)
class Position:
    x: int
    y: int


class Map:

    def __init__(self):
        self.grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.ring_on = False
        self.coat_on = False
        self.enemies = []      
        self.gollum: Optional[Position] = None
        self.mount_doom: Optional[Position] = None
        self.mithril: Optional[Position] = None

    def update_perception(self, perception_data: List[Tuple[str, int, int]]) -> None:

        pass

    def mark_danger_zones(self) -> None:

        pass

    def get_danger_radius(self, enemy_type: str) -> int:

        pass

    def is_in_bounds(self, x: int, y: int) -> bool:
        pass

    def is_safe(self, x: int, y: int) -> bool:
        pass

    def get_neighbors(self, x: int, y: int) -> List[Position]:
        pass

    def manhattan(self, a: Position, b: Position) -> int:
        pass

    def print_map(self) -> None:
        pass


def apply_ring_effects(map_obj: Map) -> None:

    pass


def apply_mithril_effects(map_obj: Map) -> None:

    pass