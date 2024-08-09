def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def isValid(row, col):
        return 0 <= row < rows and 0 <= col < cols

    def neighbours(row, col):
        indicies = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        result = []
        for r, c in indicies:
            if isValid(r, c) and grid[r][c] == "1":
                result.append((r, c))
        return result
    
    def bfs(r, c):
        queue = [(r, c)]
        visited.add((r, c))  # Mark the starting cell as visited
        while queue:
            row, col = queue.pop(0)
            for nr, nc in neighbours(row, col):
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1
    return islands






grid_t = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]]

print(numIslands(grid_t))