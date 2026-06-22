class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        chars = 'addabcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ1234567890'
        valid = {c for c in chars}

        while L < R:
            if s[L] not in valid:
                while L < R and s[L] not in valid:
                    L += 1
            if s[R] not in valid:
                while L < R and s[R] not in valid:
                    R -= 1
            
            if s[L] in valid and s[R] in valid:
                if s[L].lower() != s[R].lower():
                    return False
                L += 1
                R -= 1

        return True