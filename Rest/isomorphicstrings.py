class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping_s_to_t = {}  # Stores mapping from s to t
        mapping_t_to_s = {}  # Stores mapping from t to s
        
        for i in range(len(s)):
            if s[i] in mapping_s_to_t:
                if mapping_s_to_t[s[i]] != t[i]:
                    return False
            else:
                mapping_s_to_t[s[i]] = t[i]
                
            if t[i] in mapping_t_to_s:
                if mapping_t_to_s[t[i]] != s[i]:
                    return False
            else:
                mapping_t_to_s[t[i]] = s[i]
        
        return True


s = "bab"
t = "abb"

print(Solution().isIsomorphic(s, t))