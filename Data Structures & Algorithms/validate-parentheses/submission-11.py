class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if char in closeToOpen.keys():
                if stack and closeToOpen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            elif char in closeToOpen.values():
                stack.append(char)

        return True if not stack else False