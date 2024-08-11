def countBattleships(board):
    if not board:
        return 0
    rows, cols = len(board), len(board[0])
    number_of_battleships = 0

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == ".":
                continue
            if r > 0 and board[r-1][c] == "X":
                continue
            if c > 0 and board[r][c-1] == "X":
                continue
            else:
                number_of_battleships += 1
    return number_of_battleships


board_t = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(countBattleships(board_t))