def increasingTriplet(nums):
    if len(nums) < 3:
        return False
    i = float('inf')
    j = float('inf')
    for num in nums:
        if num < i:
            i = num
        elif num < j:
            j = num
        else:
            return True
    return False


nums_t = [1, 2, 3]
print(increasingTriplet(nums_t))