class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            letterCount = [0] * 26
            for char in string:
                pos = ord(char) - ord('a')
                letterCount[pos] += 1
            res[tuple(letterCount)].append(string)

        return list(res.values())