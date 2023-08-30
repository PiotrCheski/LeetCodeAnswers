from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
                






        for row in board:
            numbers = set()
            for elem in row:
                if elem != ".":
                    if elem in numbers:
                        return False
                    else:
                        numbers.add(elem)

        for i in range(9):
            numbers_col = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in numbers_col:
                        return False
                    else:
                        numbers_col.add(board[j][i])

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))