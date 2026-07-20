class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for bucket in reversed(freq):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res