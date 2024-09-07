import math
def isPowerOfThree(n):
    return n > 0 and 1162261467 % n == 0

n_t = 81
print(isPowerOfThree(n_t))