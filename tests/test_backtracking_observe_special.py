import io
import sys
from src.backtracking_agent import BacktrackingAgent

def test_special_line():
    fake_input = io.StringIO("My precious! Mount Doom is 10 8\n")
    sys.stdin = fake_input

    agent = BacktrackingAgent()
    agent.observe()

    if agent.map.mount_doom:
        print(f"Mount Doom recognized at ({agent.map.mount_doom.x}, {agent.map.mount_doom.y})")
    else:
        print("Mount Doom not recognized")

if __name__ == "__main__":
    test_special_line()