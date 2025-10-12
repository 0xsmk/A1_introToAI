from src.astar_agent import AStarAgent
from src.utils import Position

def test_astar_path():
    agent = AStarAgent()

    # Setup a simple environment: start (0,0), goal (3,3)
    agent.current_pos = Position(0, 0)
    agent.map.gollum = Position(3, 3)

    path = agent.a_star_search(agent.current_pos, agent.map.gollum)
    print("Planned path:")
    for p in path:
        print(f"({p.x}, {p.y})")

if __name__ == "__main__":
    test_astar_path()