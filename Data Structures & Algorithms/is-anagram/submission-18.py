class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for i in range(len(s)):
            counter[s[i]] = 1 + counter.get(s[i], 0)
            counter[t[i]] = counter.get(t[i], 0) - 1

        for value in counter.values():
            if value != 0:
                return False

        return True
