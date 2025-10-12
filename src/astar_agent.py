
# Implementation of A* search algorithm is based on:
#GeeksforGeeks DSA Guide — "A* Search Algorithm"
#https://www.geeksforgeeks.org/dsa/a-search-algorithm/

import sys
import heapq
from src.utils import Map, Position, apply_ring_effects, apply_mithril_effects


class AStarAgent:

    def __init__(self):
        self.map = Map()
        self.current_pos = Position(0, 0)
        self.goal = None
        self.has_gollum = False
        self.finished = False
        self.path_length = 0
        self.path = [] 

    def observe(self):

        try:
            line = sys.stdin.readline()
            if not line:
                return  

            line = line.strip()

            if line.startswith("My precious! Mount Doom is"):
                parts = line.split()
                if len(parts) >= 6:
                    mx, my = int(parts[-2]), int(parts[-1])
                    self.map.mount_doom = Position(mx, my)
                    self.has_gollum = True
                return

            try:
                n = int(line)
            except ValueError:
                return  # not a valid number, ignore

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

        except Exception as e:
            print("Observation error:", e, file=sys.stderr)

    def heuristic(self, a: Position, b: Position) -> int:
        return abs(a.x - b.x) + abs(a.y - b.y)

    def reconstruct_path(self, came_from, end):
        path = []
        current = end
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

    def a_star_search(self, start: Position, goal: Position):
        open_set = []
        heapq.heappush(open_set, (0, start.x, start.y, start))
        came_from = {}
        g_score = {start: 0}  
        f_score = {start: self.heuristic(start, goal)}  

        open_set_hash = {start}

        while open_set:
            _, _, _, current = heapq.heappop(open_set)
            open_set_hash.remove(current)

            if (current.x, current.y) == (goal.x, goal.y):
                return self.reconstruct_path(came_from, current)

            for neighbor in self.map.get_neighbors(current.x, current.y):
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, goal)

                    if neighbor not in open_set_hash:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor.x, neighbor.y, neighbor))
                        open_set_hash.add(neighbor)

        return []

    def decide(self):
        if not self.has_gollum and self.map.gollum:
            self.goal = self.map.gollum
        elif self.has_gollum and self.map.mount_doom:
            self.goal = self.map.mount_doom
        else:
            return None  

        if self.goal and (self.current_pos.x, self.current_pos.y) == (self.goal.x, self.goal.y):
            if not self.has_gollum:
                self.has_gollum = True
                return None
            else:
                return ("end", self.path_length)

        if not self.path or (self.path and (self.path[-1].x, self.path[-1].y) != (self.goal.x, self.goal.y)):
            self.path = self.a_star_search(self.current_pos, self.goal)

        if self.path:
            next_step = self.path.pop(0)
            self.path_length += 1
            return ("move", next_step)

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