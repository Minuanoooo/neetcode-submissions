from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        a = defaultdict(list)
        for i in strs:
            sorted_word = "".join(sorted(i))
            a[sorted_word].append(i)
        return list(a.values())