class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for string in strs:
            letterCount = [0] * 26
            for char in string:
                letterCount[(ord(char) - ord('a'))] += 1
            words[tuple(letterCount)].append(string)

        return list(words.values())