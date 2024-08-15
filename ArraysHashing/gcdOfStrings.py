def gcdOfStrings(str1, str2):
    result = ""
    letters = set()
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i] and str1[i] not in letters:
            result += str1[i]
            letters.add(str1[i])
        else:
            break
    return result

str1_t = "ABABAB"
str2_t = "ABAB"
print(gcdOfStrings(str1_t, str2_t))