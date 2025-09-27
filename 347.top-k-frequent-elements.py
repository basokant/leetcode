from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for f in reversed(freq):
            for num in f:
                res.append(num)
                if len(res) == k:
                    return res

        return res
