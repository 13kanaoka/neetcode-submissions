class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            res = min(res, nums[m])
            if nums[l] <= nums[m]: # in left side
                l = m + 1
            else: # in right side
                r = m - 1
            
        return res