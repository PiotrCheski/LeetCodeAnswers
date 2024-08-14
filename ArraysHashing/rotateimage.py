def rotate(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows):
        for col in range(row, cols):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
    for row in matrix:
        row.reverse()
    return matrix

matrix_t = [[1,2], [3, 4]]
print(rotate(matrix_t))