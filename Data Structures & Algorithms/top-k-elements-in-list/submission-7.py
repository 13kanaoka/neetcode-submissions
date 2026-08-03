class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in counter.items():
            freq[count].append(num)
        
        res = []
        for bucket in reversed(freq):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res