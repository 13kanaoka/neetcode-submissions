class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            count = [0] * 32
            for c in string:
                pos = ord('a') - ord(c)
                count[pos] += 1
            res[tuple(count)].append(string)
        return list(res.values())
            