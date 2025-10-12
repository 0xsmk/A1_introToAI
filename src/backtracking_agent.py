import sys
from src.utils import Map, Position, apply_ring_effects, apply_mithril_effects


class BacktrackingAgent:
    def __init__(self):
        self.map = Map()
        self.visited = set()
        self.path_stack = []
        self.current_pos = Position(0, 0)
        self.goal = None
        self.has_gollum = False
        self.finished = False
        self.path_length = 0

    def observe(self):
        try:
            n = int(sys.stdin.readline().strip())
            perception_data = []
            for _ in range(n):
                parts = sys.stdin.readline().strip().split()
                if len(parts) != 3:
                    continue
                symbol, x, y = parts[0], int(parts[1]), int(parts[2])
                perception_data.append((symbol, x, y))

            self.map.update_perception(perception_data)

            if self.map.mithril and (self.map.mithril.x, self.map.mithril.y) == (self.current_pos.x, self.current_pos.y):
                apply_mithril_effects(self.map)

            if self.map.gollum and not self.has_gollum:
                self.has_gollum = True
                print(f"My precious! Mount Doom is {self.map.mount_doom.x} {self.map.mount_doom.y}", flush=True)

        except Exception as e:
            print("Observation error:", e, file=sys.stderr)

    # ------------------------------------------------------------
    def decide(self):
        if not self.has_gollum and self.map.gollum:
            self.goal = self.map.gollum
        elif self.has_gollum and self.map.mount_doom:
            self.goal = self.map.mount_doom

        self.visited.add((self.current_pos.x, self.current_pos.y))

        if self.goal and (self.current_pos.x, self.current_pos.y) == (self.goal.x, self.goal.y):
            if not self.has_gollum:
                self.has_gollum = True
                self.goal = self.map.mount_doom
                return None  
            else:
                return ("end", self.path_length)

        neighbors = self.map.get_neighbors(self.current_pos.x, self.current_pos.y)
        for neighbor in neighbors:
            if (neighbor.x, neighbor.y) not in self.visited:
                self.path_stack.append(self.current_pos)
                self.path_length += 1
                return ("move", neighbor)

        if self.path_stack:
            back = self.path_stack.pop()
            self.path_length += 1
            return ("move", back)

        return None

    def act(self, action):
        if not action:
            return

        kind, value = action

        if kind == "move":
            print(f"m {value.x} {value.y}", flush=True)
            self.current_pos = value

        elif kind == "end":
            print(f"e {value}", flush=True)
            self.finished = True

    def run(self):
        while not self.finished:
            self.observe()
            action = self.decide()
            self.act(action)