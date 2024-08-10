def islandPermieter(grid):
    rows, cols = len(grid), len(grid[0])
    result = 0

    def isValid(sr, sc):
        if 0 <= sr < rows and 0 <= sc < cols:
            return True
        return False

    def neighbours(row, col):
        indices = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        result_neihbours = []
        for sr, sc in indices:
            if isValid(sr, sc) and grid[sr][sc] == 1:
                result_neihbours.append("0")
        return result_neihbours

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                result += 4
                for neighbour in neighbours(row, col):
                    result -= 1
    return result

grid_t = [[1,0]]
print(islandPermieter(grid_t))