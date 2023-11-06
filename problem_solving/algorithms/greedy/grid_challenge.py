def grid_challenge(grid):
    num_rows = len(grid)
    num_columns = len(grid[0])

    for index, row in enumerate(grid):
        grid[index] = "".join(sorted(list(row)))

    for j in range(num_columns):
        for i in range(num_rows - 1):
            if grid[i][j] > grid[i + 1][j]:
                return "NO"

    return "YES"


def test_grid_challenge():
    """Test for grid_challenge function."""
    assert grid_challenge(["abc", "ade", "efg"]) == "YES"
    assert (
        grid_challenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]) == "YES"
    )
    assert grid_challenge(["abc", "lmp", "qrt"]) == "YES"
    assert grid_challenge(["mpxz", "abcd", "wlmf"]) == "NO"
    assert grid_challenge(["abc", "hjk", "mpq", "rtv"]) == "YES"
    assert grid_challenge(["kc", "iu"]) == "YES"


test_grid_challenge()
