class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                return res
            
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
            res = min(nums[m], res)
        
        return res