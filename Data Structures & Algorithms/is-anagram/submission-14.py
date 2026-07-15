class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letterCount = {}

        for i in range(len(s)):
            letterCount[s[i]] = 1 + letterCount.get(s[i], 0)
            letterCount[t[i]] = letterCount.get(t[i], 0) - 1

        for char in letterCount:
            if letterCount[char] != 0:
                return False

        return True