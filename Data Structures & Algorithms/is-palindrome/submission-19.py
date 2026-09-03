class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isValid(s[l]):
                l += 1
            while l < r and not self.isValid(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True


    def isValid(self, char):
        if ('a' <= char <= 'z' or
            'A' <= char <= 'Z' or
            '0' <= char <= '9'):
            return True
        else:
            return False