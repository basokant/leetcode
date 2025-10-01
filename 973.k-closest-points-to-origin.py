import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(heap, [dist, x, y])
            if len(heap) > k:
                heapq.heappop(heap)

        res = [[x, y] for _, x, y in heap]
        return res
