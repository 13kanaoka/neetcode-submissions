class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        letterCount = {}

        for i in range(len(s)):
            letterCount[s[i]] = 1 + letterCount.get(s[i], 0)
            letterCount[t[i]] = letterCount.get(t[i], 0) - 1

        for key in letterCount:
            if letterCount[key] != 0: return False
        return True