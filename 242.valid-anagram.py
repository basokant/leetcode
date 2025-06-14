# @leet start
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sFreq, tFreq = Counter(s), Counter(t)

        if sFreq == tFreq:
            return True

        return False


# @leet end

