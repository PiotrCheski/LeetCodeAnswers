def equalPairs(grid):
    rows, cols = len(grid), len(grid[0])
    row_count = {}
    result = 0

    for row in grid:
        row_tuple = tuple(row)
        if row_tuple in row_count:
            row_count[row_tuple] += 1
        else:
            row_count[row_tuple] = 1
    
    for col in range(cols):
        col_tuple = tuple(grid[row][col] for row in range(rows))
        if col_tuple in row_count:
            result += row_count[col_tuple]
    return result

grid_t = [[13,13], [13, 13]]
print(equalPairs(grid_t))