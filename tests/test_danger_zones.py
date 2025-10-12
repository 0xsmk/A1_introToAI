from src.utils import Map, Position, ORC, URUK, NAZGUL, WATCHTOWER

def test_danger_zones():
    game_map = Map()

    game_map.enemies = [
        {"type": ORC, "pos": Position(5, 5)},
        {"type": URUK, "pos": Position(2, 2)},
        {"type": NAZGUL, "pos": Position(8, 8)},
    ]

    # Case 1: No ring, no mithril
    print("=== Case 1: Base map (no ring, no mithril) ===")
    game_map.mark_danger_zones()
    game_map.print_map()

    # Case 2: With Mithril
    print("\n=== Case 2: With Mithril ===")
    game_map.coat_on = True
    game_map.mark_danger_zones()
    game_map.print_map()

    # Case 3: With Ring On
    print("\n=== Case 3: With Ring On ===")
    game_map.ring_on = True
    game_map.mark_danger_zones()
    game_map.print_map()

if __name__ == "__main__":
    test_danger_zones()