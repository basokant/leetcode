import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        while low <= high:
            k = (low + high) // 2

            hours = 0
            for pile in piles:
                hours += int(math.ceil(float(pile) / k))

            if hours <= h:
                res = k
                high = k - 1
            else:
                low = k + 1

        return res
