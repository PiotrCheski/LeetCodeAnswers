def maxVowels(s, k):
    vowels = set("aeiou")
    max_vowels = 0
    current_vowels = 0
    for i in range(k):
        if s[i] in vowels:
            current_vowels += 1
        max_vowels = current_vowels
    for i in range(k, len(s)):
        if s[i] in vowels:
            current_vowels += 1
        if s[i - k] in vowels:
            current_vowels -= 1
        max_vowels = max(max_vowels, current_vowels)
s_t = "abciiidef"
k_t = 3
print(maxVowels(s_t, k_t))