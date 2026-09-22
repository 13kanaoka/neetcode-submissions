class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, total, currArr):
            if total == target:
                res.append(currArr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            currArr.append(nums[i])
            backtrack(i, total + nums[i], currArr)

            currArr.pop()
            backtrack(i + 1, total, currArr)

        backtrack(0, 0, [])
        return res