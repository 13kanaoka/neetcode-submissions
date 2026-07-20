class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        for i in range(len(s)):
            seen[s[i]] = 1 + seen.get(s[i], 0)
            seen[t[i]] = seen.get(t[i], 0) - 1

        for value in seen.values():
            if value != 0:
                return False

        return True