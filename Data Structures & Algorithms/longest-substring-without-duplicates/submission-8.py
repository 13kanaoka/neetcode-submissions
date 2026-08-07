class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        longest = 0

        l = 0
        for r in range(len(s)):
            while l < r and s[r] in charSet: # l < r required?
                charSet.discard(s[l])
                l += 1
            
            charSet.add(s[r])
            longest = max(longest, r - l + 1)

        return longest