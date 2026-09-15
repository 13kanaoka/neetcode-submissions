class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(total, i, currArr):
            if total == target:
                res.append(currArr.copy())
                return
            if i >= len(nums) or total > target:
                return

            currArr.append(nums[i])
            backtrack(total + nums[i], i, currArr)

            currArr.pop()
            backtrack(total, i + 1, currArr)
        
        backtrack(0, 0, [])
        return res