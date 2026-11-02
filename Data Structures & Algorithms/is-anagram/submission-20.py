class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for i in range(len(s)):
            schar = s[i]
            tchar = t[i]

            count[schar] = 1 + count.get(schar, 0)
            count[tchar] = count.get(tchar, 0) - 1

        for key, value in count.items():
            if value != 0:
                return False
        return True