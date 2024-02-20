mat_test = [[1,2,3],[4,5,6],[7,8,9]]
mat_test2 = [[1,1,1,1],
             [1,1,1,1],
             [1,1,1,1],
             [1,1,1,1]]
mat_test3 = [[5]]
def solve(mat):
    res = 0
    for i in range(len(mat)):
        res += mat[i][i]
        res += mat[i][len(mat[i])-1-i]
    if len(mat) % 2 != 0:
        mid_index = (len(mat)-1) // 2
        res -= mat[mid_index][mid_index]
    return res



print(solve(mat_test3))