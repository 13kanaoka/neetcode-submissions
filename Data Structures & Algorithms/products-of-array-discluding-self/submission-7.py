class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        offset = 1
        for i in range(len(res)):
            res[i] *= offset
            offset *= nums[i]
        
        offset = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= offset
            offset *= nums[i]

        return res