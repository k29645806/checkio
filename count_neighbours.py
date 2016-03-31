grid = ((1, 0, 0, 1, 0),
        (0, 1, 0, 0, 0),
        (0, 0, 1, 0, 1),
        (1, 0, 0, 0, 0),
        (0, 0, 1, 0, 0),)

def count_neighbours(grid, row, col):
    n_x = len(grid)
    n_y = len(grid[0])
    NEIGHBORS = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1))
    result = 0
    for step in NEIGHBORS:
        dx, dy = step
        x_index = row + dx
        y_index = col + dy
        if x_index in range(n_x) and y_index in range(n_y):
            item = grid[x_index][y_index]
            result += item
    return result

print count_neighbours(grid,1,2)
