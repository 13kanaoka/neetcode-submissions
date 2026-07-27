class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = len(nums)
        for i in range(len(nums)):
            xorr = xorr ^ nums[i] ^ i
        
        return xorr