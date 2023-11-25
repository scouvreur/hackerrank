# reducing the tower to height 1 is always the optimal move
# the winner depends on the number of towers remaining


def tower_breakers(num_towers, tower_height):
    if num_towers % 2 == 0 or tower_height == 1:
        return 2
    else:
        return 1


def test_tower_breakers():
    """Test for tower_breakers function."""
    assert tower_breakers(2, 2) == 2
    assert tower_breakers(1, 4) == 1


test_tower_breakers()
