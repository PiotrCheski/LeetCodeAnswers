def findComplement(num):
    mask = (1 << num.bit_length()) - 1
    return num ^ mask

num_t = 5
print(findComplement(num_t))