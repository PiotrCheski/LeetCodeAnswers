def mergeAlternately(word1, word2):
    output = ""
    for i in range(min(len(word1), len(word2))):
        output += word1[i]
        output += word2[i]
    for i in range(min(len(word1), len(word2)), max(len(word1), len(word2))):
        if len(word1) > len(word2):
            output += word1[i]
        elif len(word1) < len(word2):
            output += word2[i]
        else:
            continue
    return output

word1_t = "ab"
word2_t = "pqrs"
print(mergeAlternately(word1_t, word2_t))

