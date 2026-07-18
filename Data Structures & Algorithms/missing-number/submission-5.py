class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = 0
        for i in range(len(nums) + 1): xorr ^= i
        for num in nums: xorr ^= num

        return xorr