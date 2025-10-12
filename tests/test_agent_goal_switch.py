from src.backtracking_agent import BacktrackingAgent
from src.utils import Position

def test_goal_switch():
    agent = BacktrackingAgent()

    agent.map.gollum = Position(3, 3)
    agent.current_pos = Position(3, 3)

    action = agent.decide()
    print("After finding Gollum:", action, "has_gollum =", agent.has_gollum)

    agent.map.mount_doom = Position(8, 8)
    agent.has_gollum = True

    action = agent.decide()
    print("After knowing Mount Doom:", action)

    agent.current_pos = Position(8, 8)
    action = agent.decide()
    print("After reaching Mount Doom:", action)

if __name__ == "__main__":
    test_goal_switch()