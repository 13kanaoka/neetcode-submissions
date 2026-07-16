class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            while not self.validityChecker(s[left]) and left < right:
                left += 1
            while not self.validityChecker(s[right]) and left < right:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def validityChecker(self, char):
        if ('a' <= char <= 'z' or
            'A' <= char <= 'Z' or
            '0' <= char <= '9'):
            return True
        else:
            return False