from src.utils import Map, Position

def test_full_map_update():
    game_map = Map()

    perception_round_1 = [
        ('O', 5, 5),   # Orc
        ('U', 2, 8),   # Uruk-hai
        ('C', 6, 3),   # Mithril
    ]

    print("\n=== Round 1: initial perception ===")
    game_map.update_perception(perception_round_1)
    game_map.print_map()

    perception_round_2 = [
        ('N', 8, 8),   # Nazgûl
        ('G', 10, 10)  # Gollum
    ]

    print("\n=== Round 2: new perception with Nazgûl and Gollum ===")
    game_map.update_perception(perception_round_2)
    game_map.print_map()

    print("\n=== Round 3: Mithril picked up (coat_on = True) ===")
    game_map.coat_on = True
    game_map.mark_danger_zones()
    game_map.print_map()

    print("\n=== Round 4: Ring ON ===")
    game_map.ring_on = True
    game_map.mark_danger_zones()
    game_map.print_map()

if __name__ == "__main__":
    test_full_map_update()