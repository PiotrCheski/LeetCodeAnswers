class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        arr = [elem for elem in arr if elem != ""]
        if arr:
            return len(arr[-1])
        else:
            return 0

tests = " this is your job   "
print(Solution().lengthOfLastWord(tests))