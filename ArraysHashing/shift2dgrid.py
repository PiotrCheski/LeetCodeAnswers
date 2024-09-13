def shiftGrid(grid, k):
    ROWS = len(grid)
    COLS = len(grid[0])
    tmp = 0
    tmp2 = grid[0][0]
    for i in range(k):
        for row in range(ROWS):
            for col in range(COLS):
                print(grid[row][col])
                if row == 0 and col == 0:
                    tmp = grid[ROWS-1][COLS-1]
                    grid[row][col] = tmp
                else:
                    tmp = grid[row][col]
                    grid[row][col] = tmp2
                    tmp2 = tmp
    return grid

grid_t = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k_t = 4
print(shiftGrid(grid_t, k_t))