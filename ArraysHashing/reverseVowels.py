def reverseVowels(s):
    queue = []
    vowels = set("aeiouAEIOU")
    result = ""
    for char in s:
        if char in vowels:
            queue.append(char)

    for char in s:
        if char in vowels:
            result += queue.pop()
        else:
            result += char
    return result

s_t = "hello"
print(reverseVowels(s_t))