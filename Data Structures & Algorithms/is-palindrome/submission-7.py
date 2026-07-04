class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789'

        left, right = 0, len(s)-1

        while left <= right:
            while s[left] not in valid and left < right:
                left += 1
            while s[right] not in valid and left < right:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True