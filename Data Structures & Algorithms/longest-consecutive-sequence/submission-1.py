class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
            curr = 0
            if (num - 1) not in seen:
                start = num
                curr = 1
            
            while (num + 1) in seen:
                curr += 1
                num = num + 1
            longest = max(longest, curr)

        return longest
            