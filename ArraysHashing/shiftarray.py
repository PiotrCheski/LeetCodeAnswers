def shiftGrid(grid, k):
    ROWS = len(grid) -1
    #COLS = len(grid[0])
    tmp = grid[ROWS]
    tmp2 = grid[0]
    for i in range(ROWS + 1):
        if i == 0:
            grid[i] = tmp
        else:
            tmp = grid[i]
            grid[i] = tmp2
            tmp2 = tmp
    return grid


grid_t = [5,8,3,2]
k_t = 1
print(shiftGrid(grid_t, k_t))