def judgeCircle(moves):
    pos_x, pos_y = 0, 0
    for move in moves:
        if move == "R":
            pos_x += 1
        elif move == "L":
            pos_x -= 1
        elif move == "U":
            pos_y += 1
        elif move == "D":
            pos_y -= 1
    if pos_x == 0 and pos_y == 0:
        return True
    return False


moves_t = "LL"
print(judgeCircle(moves_t))