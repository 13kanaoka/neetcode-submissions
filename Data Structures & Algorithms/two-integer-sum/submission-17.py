class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            find = target - nums[i]

            if find in seen:
                return [seen[find], i]
            seen[nums[i]] = i