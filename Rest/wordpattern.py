class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping_pattern_to_s = {}
        mapping_s_to_pattern = {}
        s = s.split(" ")

        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            if pattern[i] in mapping_pattern_to_s:
                if mapping_pattern_to_s[pattern[i]] != s[i]:
                    return False
            else:
                mapping_pattern_to_s[pattern[i]] = s[i]
            if s[i] in mapping_s_to_pattern:
                if mapping_s_to_pattern[s[i]] != pattern[i]:
                    return False
            else:
                mapping_s_to_pattern[s[i]] = pattern[i]
        return True
    
pattern = "aaa"
s = "aa aa aa aa"

print(Solution().wordPattern(pattern, s))