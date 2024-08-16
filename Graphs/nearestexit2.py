def nearestExit(maze, entrance):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = [(entrance[0], entrance[1], 0)]  # Queue stores (row, col, distance)
    visited.add((entrance[0], entrance[1]))
    
    def isValid(row, col):
        return 0 <= row < rows and 0 <= col < cols
    
    def isExit(row, col):
        # It's an exit if it's on the boundary and not the entrance
        return (row == 0 or row == rows - 1 or col == 0 or col == cols - 1) and (row, col) != (entrance[0], entrance[1])
    
    while queue:
        row, col, dist = queue.pop(0)  # Dequeue operation
        
        # Check all 4 possible directions
        for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if isValid(r, c) and (r, c) not in visited and maze[r][c] == ".":
                if isExit(r, c):
                    return dist + 1  # Return the distance as soon as we find an exit
                queue.append((r, c, dist + 1))  # Enqueue operation
                visited.add((r, c))
    
    return -1  # If no exit is found

# Test case
maze_t = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance_t = [1,2]
print(nearestExit(maze_t, entrance_t))
