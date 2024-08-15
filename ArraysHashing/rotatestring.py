def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    double_s = s + s
    if goal_t in double_s:
        return True
    return False

s_t = "ab"
goal_t = "ba"
print(rotateString(s_t, goal_t))