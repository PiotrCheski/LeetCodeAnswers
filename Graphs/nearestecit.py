def nearestExit(maze, entrance):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    result = 0
    entrance_neighbours = [(entrance[0] - 1, entrance[1]), (entrance[0] + 1, entrance[1]), (entrance[0], entrance[1] - 1), (entrance[0], entrance[1] + 1)]
    queue = [(entrance[0], entrance[1])]
    visited.add((entrance[0], entrance[1]))
    def isValid(row, col):
        return 0 <= row < rows and 0 <= col < cols
    
    def neighbours(row, col):
        indicies = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        result_neighbours = []
        result_out_of_maze = []
        for r, c in indicies:
            if isValid(r, c) and maze[r][c] == ".":
                result_neighbours.append((r, c))
            elif not isValid(r, c):
                result_out_of_maze.append((r, c))
        return result_neighbours, result_out_of_maze
    
    while queue:
        row, col = queue.pop(0)
        neighbours, out_of_maze = neighbours(row, col)
        for nr, nc in out_of_maze:
            if (nr, nc) not in entrance_neighbours:
                return result
        for nr, nc in neighbours:
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
                result += 1
    return -1

maze_t = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance_t = [1,2]
print(nearestExit(maze_t, entrance_t))