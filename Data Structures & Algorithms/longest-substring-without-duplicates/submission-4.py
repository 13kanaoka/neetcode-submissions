class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        longest = 0
        left = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.discard(s[left])
                left += 1
            charSet.add(s[right])

            currLength = right - left + 1
            longest = max(longest, currLength)
        
        return longest