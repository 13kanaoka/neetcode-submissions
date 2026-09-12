class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(currSum, currArr, i):
            if currSum == target:
                res.append(currArr.copy())
                return
            if i >= len(nums) or currSum > target:
                return
            
            currArr.append(nums[i])
            backtrack(currSum + nums[i], currArr, i)

            currArr.pop()
            backtrack(currSum, currArr, i + 1)
        
        backtrack(0, [], 0)
        return res