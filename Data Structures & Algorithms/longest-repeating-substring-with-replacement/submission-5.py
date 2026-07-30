class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counter = {}
   
        left = 0
        for right in range(len(s)):
            counter[s[right]] = 1 + counter.get(s[right], 0)

            while (right - left + 1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        return longest
