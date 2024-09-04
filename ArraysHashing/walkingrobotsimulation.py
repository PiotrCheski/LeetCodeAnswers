def robotSim(commands, obstacles):
    POS_X = 0
    POS_Y = 0
    MODE = 0
    output = 0
    for idx, number in enumerate(commands):
        if number >= 1 and number <= 9:
            if MODE == 0:
                POS_Y += number
                possible_next_location = [POS_X, POS_Y]
                if possible_next_location in obstacles:
                    POS_Y -= number
                    break
            elif MODE == -1:
                POS_X += number
                possible_next_location = [POS_X, POS_Y]
                if possible_next_location in obstacles:
                    POS_X -= number
                    break
            elif MODE == -2:
                POS_X -= number
                possible_next_location = [POS_X, POS_Y]
                if possible_next_location in obstacles:
                    POS_X += number
                    break
        elif number == -1:
            MODE = -1
        elif number == -2:
            MODE =- 2
        print(POS_X, POS_Y)
        euclidian_distance = POS_X**2 + POS_Y**2
        output = max(euclidian_distance, output)
    return output

commands_t = [6,-1,-1,6]
obstacles_t = []
print(robotSim(commands_t, obstacles_t))