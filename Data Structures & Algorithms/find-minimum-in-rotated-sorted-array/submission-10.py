class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break
            
            minimum = min(minimum, nums[m])
            if nums[l] <= nums[m]:
                # we are in left
                l = m + 1
            elif nums[l] > nums[m]:
                # we are in right
                r = m - 1
            
        return minimum