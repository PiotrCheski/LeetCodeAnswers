def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    fresh_oranges = 0
    time = 0
    queue = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh_oranges += 1
            elif grid[r][c] == 2:
                queue.append((r, c))
            else:
                continue

    def isValid(row, col):
        return 0 <= row < rows and 0 <= col < cols
    
    def neighbours(row, col):
        indicies = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        result = []
        for r, c in indicies:
            if isValid(r, c) and grid[r][c] == 1:
                result.append((r, c))
        return result

    if fresh_oranges == 0:
        return 0

    while len(queue) > 0:
        for i in range(len(queue)):
            row, col = queue.pop(0)
            for nr, nc in neighbours(row, col):
                grid[nr][nc] = 2
                fresh_oranges -= 1
                queue.append((nr, nc))
        if queue:
            time += 1
    if fresh_oranges == 0:
        return time
    else:
        return -1

grid_t = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid_t))