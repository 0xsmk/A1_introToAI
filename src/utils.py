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
        for symbol, x, y in perception_data:
            if not self.is_in_bounds(x, y):
                continue
            self.grid[x][y] = symbol

            if symbol == GOLLUM:
                self.gollum = Position(x, y)
            elif symbol == MOUNT_DOOM:
                self.mount_doom = Position(x, y)
            elif symbol == MITHRIL:
                self.mithril = Position(x, y)

            elif symbol in [ORC, URUK, NAZGUL, WATCHTOWER]:
                already_known = any(
                    e["pos"].x == x and e["pos"].y == y and e["type"] == symbol
                    for e in self.enemies
                )
                if not already_known:
                    self.enemies.append({"type": symbol, "pos": Position(x, y)})
        self.mark_danger_zones()
        print("Enemies list:", [(e["type"], e["pos"].x, e["pos"].y) for e in self.enemies])


    def mark_danger_zones(self) -> None:

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] == DANGER:
                    self.grid[i][j] = EMPTY

        for enemy in self.enemies:
            e_type = enemy["type"]
            ex, ey = enemy["pos"].x, enemy["pos"].y
            radius = self.get_danger_radius(e_type)

            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):
                    nx, ny = ex + dx, ey + dy

                    if dx == 0 and dy == 0:
                        continue

                    if not self.is_in_bounds(nx, ny):
                        continue

                    if self.grid[nx][ny] in [GOLLUM, MOUNT_DOOM, MITHRIL, ORC, URUK, NAZGUL, WATCHTOWER]:
                        continue

                    self.grid[nx][ny] = DANGER        


    def get_danger_radius(self, enemy_type: str) -> int:
        base_radius = {ORC:1, URUK:2, NAZGUL:1, WATCHTOWER:2}
        r = base_radius.get(enemy_type, 0)

        if self.coat_on:
            if enemy_type in (ORC, URUK):
                r = max(0, r - 1)
            elif enemy_type == NAZGUL:
                r = 1

        if self.ring_on:
            if enemy_type in [ORC, URUK]:
                r = max(0, r - 1)
            elif enemy_type in [NAZGUL, WATCHTOWER]:
                r += 1

        return r            


    def is_in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE

    def is_safe(self, x: int, y: int) -> bool:
        pass

    def get_neighbors(self, x: int, y: int) -> List[Position]:
        neighbors = []

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if self.is_in_bounds(nx, ny):
                neighbors.append(Position(nx, ny))
        return neighbors

    def manhattan(self, a: Position, b: Position) -> int:
        return abs(a.x - b.x) + abs(a.y - b.y)

    def print_map(self) -> None:
        """
        Print the current 13×13 map in the console.
        Each cell shows its current symbol (., P, O, G, etc.).
        """
        print("    " + " ".join(f"{j:2}" for j in range(GRID_SIZE)))
        print("   " + "---" * GRID_SIZE)
        for i in range(GRID_SIZE):
            row = " ".join(f"{self.grid[i][j]:2}" for j in range(GRID_SIZE))
            print(f"{i:2} | {row}")


def apply_ring_effects(map_obj: Map) -> None:

    pass


def apply_mithril_effects(map_obj: Map) -> None:

    pass