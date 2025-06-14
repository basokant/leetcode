# @leet start
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numsFreq = defaultdict(int)

        for num in nums:
            numsFreq[num] += 1

        return sorted(numsFreq, key=numsFreq.get, reverse=True)[:k]


# @leet end
