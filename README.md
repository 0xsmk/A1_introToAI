# Assignment 1 — Intro to AI  
**Project:** Ring Destroyer  

Implementation of an intelligent agent that explores and navigates a 13×13 grid world to reach Gollum and then Mount Doom, while avoiding enemies and adapting to dynamic danger zones. Two approaches are implemented: Backtracking (DFS) and A* Search.

---

## Overview

Frodo operates in a 13×13 world with:
- Orcs (O), Uruk-hai (U), Nazgûl (N), Watchtowers (W)
- Gollum (G), Mount Doom (M), Mithril coat (C)

Enemies generate danger zones (P) depending on:
- whether the Ring is worn (`ring_on`)
- or Mithril is worn (`coat_on`)

The goal:
1. Safely reach Gollum (G)  
2. Receive Mount Doom (M) coordinates  
3. Navigate to M using Backtracking or A*  
4. End the mission (`e k`)

---

## Components

| File | Description |
|------|--------------|
| `utils.py` | Map representation, danger zones, perception updates, Ring/Mithril effects |
| `backtracking_agent.py` | DFS-based exploration and goal switching |
| `astar_agent.py` | Optimal A* pathfinding (based on GeeksforGeeks A* Search guide) |
| `tests/` | Offline tests for all modules |

---

## Algorithms

### Backtracking Agent
- Explores safely with DFS
- Avoids revisiting dangerous cells
- Switches goals automatically (G → M)
- Uses map functions: `get_neighbors`, `is_safe`, `update_perception`, `mark_danger_zones`

### A* Agent
- Computes the shortest safe path using Manhattan heuristic  
- f = g + h  
  - g: cost from start  
  - h: heuristic (Manhattan)  
- Implementation adapted from:  
  GeeksforGeeks DSA Guide — "A* Search Algorithm"  
  https://www.geeksforgeeks.org/dsa/a-search-algorithm/

---


## Running Tests

Run each module independently without the official interactor.

- python3 -m tests.test_danger_zones
- python3 -m tests.test_full_map_update
- python3 -m tests.test_backtracking_agent_offline
- python3 -m tests.test_astar_agent_offline

---

## Example Output (A* Agent)

Planned path:
(0, 1)
(0, 2)
(0, 3)
(1, 3)
(2, 3)
(3, 3)

---

## Key Topics
- Pathfinding (DFS, A*)
- Heuristic design
- Safe state exploration
- Dynamic danger recalculation (Ring & Mithril)
- Agent control loop (`observe → decide → act`)

---

## References
- Assignment 1 — Intro to AI (Ring Destroyer)
- GeeksforGeeks: A* Search Algorithm  
  https://www.geeksforgeeks.org/dsa/a-search-algorithm/
- Python documentation (`heapq`, `dataclasses`, `sys.stdin`)

## Author
Mikhail Shumakov (B24-CSE-07, Innopolis University)