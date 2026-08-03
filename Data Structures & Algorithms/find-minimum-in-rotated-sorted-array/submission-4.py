class Solution:
    def findMin(self, nums: List[int]) -> int:
        # init l, r = 0, len(nums) - 1
        # least = s[0]
        # m = (r + l) // 2
        # if l < m < r -> return l
        # if l < m -> left side
        #   if l > m -> right side
        # check min(least, m)

        least = nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[l] < nums[r]:
                least = min(least, nums[l])
                break

            least = min(least, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return least