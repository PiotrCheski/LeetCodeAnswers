def robotSim(commands, obstacles):
    pos_x = 0
    pos_y = 0
    mode = 0
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    obstacles_set = set(map(tuple, obstacles))
    max_distance = 0
    for command in commands:
        if command == -2:
            mode = (mode - 1) % 4
        elif command == -1:
            mode = (mode + 1) % 4
        else:
            dx, dy = DIRECTIONS[mode]
            for _ in range(command):
                next_pos_x, next_pos_y = pos_x + dx, pos_y + dy
                if (next_pos_x, next_pos_y) not in obstacles_set:
                    pos_x, pos_y = next_pos_x, next_pos_y
                    max_distance = max(max_distance, pos_x **2 + pos_y**2)
                else:
                    break
    return max_distance

commands_t = [6,-1,-1,6]
obstacles_t = []
print(robotSim(commands_t, obstacles_t))