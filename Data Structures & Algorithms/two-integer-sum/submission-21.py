class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in numSet:
                return [numSet[difference], i]
            
            numSet[nums[i]] = i
