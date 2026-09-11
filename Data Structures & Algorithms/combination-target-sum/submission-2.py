class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, currList):
            if total == target:
                res.append(currList.copy())
                return
            if i >= len(nums) or total > target:
                return

            currList.append(nums[i])
            dfs(i, total + nums[i], currList)
            
            currList.pop()
            dfs(i + 1, total, currList)
            
        dfs(0, 0, [])
        return res