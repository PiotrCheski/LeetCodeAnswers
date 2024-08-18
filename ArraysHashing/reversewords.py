def reverseWord(s):
    result = " ".join(reversed(s.split()))
    return result
s_t="the sky"
print(reverseWord(s_t))