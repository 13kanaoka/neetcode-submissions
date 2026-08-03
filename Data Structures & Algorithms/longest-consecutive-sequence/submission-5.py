class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in range(len(nums)):
            if (nums[i] - 1) not in numSet:
                curr = 1
                while (nums[i] + curr) in numSet:
                    curr += 1
                longest = max(longest, curr)

        return longest