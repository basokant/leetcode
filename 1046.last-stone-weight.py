import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stone = [-s for s in stones]
        heapq.heapify(stone)

        while len(stone) > 1:
            y = heapq.heappop(stone)
            x = heapq.heappop(stone)

            if x != y:
                heapq.heappush(stone, y - x)

        return -heapq.heappop(stone) if stone else 0
