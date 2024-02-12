words_test = ["abc","bcd","aaaa","cbc"]
x_test = "z"


def findWordsContaining(words, x):
    res = []
    for idx, word in enumerate(words):
        for char in word:
            if char==x:
                res.append(idx)
                break
    return res

print(findWordsContaining(words_test, x_test))