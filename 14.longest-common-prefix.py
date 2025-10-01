class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""

        length = min(len(s) for s in strs)

        for i in range(length):
            if not all(s[i] == strs[0][i] for s in strs):
                return prefix
            prefix += strs[0][i]

        return prefix
