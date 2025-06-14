# @leet start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs_table = defaultdict(list)

        for string in strs:
            sorted_string = "".join(sorted(string))
            strs_table[sorted_string].append(string)

        return list(strs_table.values())


# @leet end

