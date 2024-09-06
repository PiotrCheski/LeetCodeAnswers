def countSymmetricIntegers(low, high):
    output = 0
    for number in range(low, high + 1):
        string_number = str(number)
        if len(string_number) % 2 == 0:
            midpoint = len(string_number) // 2
            first_half_sum = sum(int(digit) for digit in string_number[:midpoint])
            second_half_sum = sum(int(digit) for digit in string_number[midpoint:])
            
            if first_half_sum == second_half_sum:
                output += 1
    return output


low_t = 1
high_t = 120
print(countSymmetricIntegers(low_t, high_t))