class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            seen[s_char] = 1 + seen.get(s_char, 0)
            seen[t_char] = seen.get(t_char, 0) - 1

        for value in seen.values():
            if value != 0:
                return False

        return True