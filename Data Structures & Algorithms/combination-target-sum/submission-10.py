class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(total, currArr, i):
            if total == target:
                res.append(currArr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            currArr.append(nums[i])
            backtrack(total + nums[i], currArr, i)

            currArr.pop()
            backtrack(total, currArr, i + 1)

            return
        
        backtrack(0, [], 0)
        return res