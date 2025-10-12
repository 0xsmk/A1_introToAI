from src.backtracking_agent import BacktrackingAgent
from src.utils import Position

def test_agent_offline():
    agent = BacktrackingAgent()


    perception_data_1 = [
        ('.', 0, 1),
        ('.', 1, 0),
        ('O', 2, 2),  # Orc nearby
        ('G', 3, 3)   # Gollum far away
    ]

    agent.map.update_perception(perception_data_1)
    agent.map.print_map()

    action = agent.decide()
    print("\nAgent decided:", action)

    if action and action[0] == "move":
        print(f"Performing move to {action[1].x}, {action[1].y}")
        agent.act(action)
        agent.map.print_map()

if __name__ == "__main__":
    test_agent_offline()