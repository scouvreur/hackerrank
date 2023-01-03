grid = ["1112", "1912", "1892", "1234"]
# grid = ["989", "191", "111"]
new_grid = []
for line in grid:
    new_grid.append(list(line))
grid = new_grid


def is_cavity(i, j, grid):
    if (
        grid[i][j] > grid[i - 1][j]
        and grid[i][j] > grid[i][j - 1]
        and grid[i][j] > grid[i + 1][j]
        and grid[i][j] > grid[i][j + 1]
    ):
        return True
    else:
        return False


# cavities = [(1,1), (2,2)]
cavities = []

for i in range(len(grid)):
    for j in range(len(grid)):
        # exclude grid edges
        if i > 0 and i != len(grid) - 1 and j > 0 and j != len(grid) - 1:
            # print(i, j, grid[i][j])
            if is_cavity(i, j, grid):
                cavities.append((i, j))

for cavity in cavities:
    grid[cavity[0]][cavity[1]] = "X"

result = []
for line in grid:
    result.append("".join(line))
