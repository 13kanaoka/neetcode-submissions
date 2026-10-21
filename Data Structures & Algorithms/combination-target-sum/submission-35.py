class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currTotal, currArr):
            if currTotal == target:
                res.append(currArr.copy())
                return
            if i >= len(nums) or currTotal > target:
                return
            
            currArr.append(nums[i])
            dfs(i, currTotal + nums[i], currArr)

            currArr.pop()
            dfs(i + 1, currTotal, currArr)

        dfs(0, 0, [])
        return res