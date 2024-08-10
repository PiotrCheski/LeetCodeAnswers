def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    maxArea = 0

    def isValid(row, col):
        return 0 <= row < rows and 0 <= col < cols

    def neighbours(row, col):
        indicies = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        result = []
        for r, c in indicies:
            if isValid(r, c) and grid[r][c] == 1:
                result.append((r, c))
        return result
    

    def bfs(r, c):
        queue = [(r, c)]
        visited.add((r, c))
        maxArea_local = 1
        while queue:
            row, col = queue.pop(0)
            for nr, nc in neighbours(row, col):
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    maxArea_local += 1
        return maxArea_local
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                maxArea = max(maxArea, bfs(r, c))
    return maxArea
    
grid_t = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(numIslands(grid_t))