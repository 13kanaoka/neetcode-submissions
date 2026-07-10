class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if char not in closeToOpen:
                stack.append(char)
            elif char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
