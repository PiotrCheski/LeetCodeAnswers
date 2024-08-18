def increasingTriplet(nums):
    if len(nums) < 3:
        return False

    first = float('inf')
    second = float('inf')

    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    
    return False


nums_t = [1, 2, 3]
print(increasingTriplet(nums_t))