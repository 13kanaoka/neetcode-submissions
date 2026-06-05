class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary with value -> index
        seen = {}

        for i in range(len(nums)):
            curr = target - nums[i]

            if curr in seen:
                return [seen[curr], i]
            
            seen[nums[i]] = i