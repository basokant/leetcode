class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])

            area = w * h
            res = max(res, area)

            if height[left] <= height[right]:
                left += 1
            else
                right -= 1

        return res
