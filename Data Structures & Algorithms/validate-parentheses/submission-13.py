class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stack = []

        for char in s:
            if char in openToClose.values():
                stack.append(char)
            if char in openToClose.keys():
                if stack and stack[-1] == openToClose[char]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False