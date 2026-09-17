class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for c in string:
                pos = ord(c) - ord('a')
                count[pos] += 1
            res[tuple(count)].append(string)
        
        return list(res.values())