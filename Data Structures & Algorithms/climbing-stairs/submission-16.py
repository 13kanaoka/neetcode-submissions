class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def decisionTree(curr):
            if curr == n:
                return 1
            elif curr > n:
                return 0

            if curr in memo:
                return memo[curr]
            
            memo[curr] = (decisionTree(curr + 1) + decisionTree(curr + 2))
            return memo[curr]

        return decisionTree(0)