def canConstruct(ransomNote, magazine):
    if len(ransomNote) > len(magazine):
        return False
    
    dict_rn = {}
    dict_mg = {}

    for char in magazine:
        if char in dict_mg:
            dict_mg[char] += 1
        else:
            dict_mg[char] = 1

    for char in ransomNote:
        if char in dict_rn:
            dict_rn[char] += 1
            if dict_rn[char] > dict_mg[char]:
                return False
        else:
            dict_rn[char] = 1
            if char not in dict_mg or dict_rn[char] > dict_mg[char]:
                return False
    return True

ransomNote_t = "aab"
magazine_t = "aac"
print(canConstruct(ransomNote_t,magazine_t))
