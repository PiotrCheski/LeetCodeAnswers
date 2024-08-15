def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    result = []

    for num in candies:
        curr_num = num + extraCandies
        if curr_num >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result

candies_t = [2,3,5,1,3]
extraCandies_t = 3
print(kidsWithCandies(candies_t, extraCandies_t))