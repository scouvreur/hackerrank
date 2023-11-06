def truck_tour(petrolpumps):
    num_pumps = len(petrolpumps)
    min_possible_starts = num_pumps - 1

    # try starts from all pumps
    for start in range(num_pumps):
        # start with no fuel
        fuel = 0
        # attempt to go around
        for i in range(num_pumps):
            pump = (start + i) % num_pumps
            # get fuel from pump
            fuel += petrolpumps[pump][0]
            # spend fuel to get to next one
            fuel -= petrolpumps[pump][1]

            # if fuel runs to zero, stop
            if fuel < 0:
                break

            # if reaches the end, add start as possible
            if (pump + 1) % num_pumps == start:
                min_possible_starts = min(min_possible_starts, start)

    return min_possible_starts


def test_truck_tour():
    """Test for truck_tour function."""
    assert truck_tour([[1, 5], [10, 3], [3, 4]]) == 1


test_truck_tour()
