def addDigits(num):
    if num <= 9:
        return num
    else:
        return (num - 1) % 9 + 1

num_t = 11
print(addDigits(num_t))