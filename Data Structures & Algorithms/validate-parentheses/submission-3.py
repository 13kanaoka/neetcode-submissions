class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        valid = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if stack and char in valid.keys():
                if stack[-1] == valid[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False