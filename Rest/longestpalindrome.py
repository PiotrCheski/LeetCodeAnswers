def longestPalindrome(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    letters = {}
    output = 0

    for char in s:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    odd_found = False
    for value in letters.values():
        if value % 2 == 0:
            output += value
        else:
            output += value - 1 
            odd_found = True 

    if odd_found:
        output += 1

    return output

s_t = "ccc"
print(longestPalindrome(s_t))