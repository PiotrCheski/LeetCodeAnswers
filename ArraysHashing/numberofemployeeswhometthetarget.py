hours_test = [0,1,2,3,4]
k_test = 2

def solve(hours, target):
    res = 0
    for hour in hours:
        if hour >= target:
            res += 1
    return res
print(solve(hours_test, k_test))