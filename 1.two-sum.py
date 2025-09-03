class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numToIdxMap = dict((num, idx) for idx, num in enumerate(nums))

        for idx, num in enumerate(nums):
            otherNum = target - num
            otherIdx = numToIdxMap[otherNum] if otherNum in numToIdxMap else -1
            if otherIdx > 0 and otherIdx != idx:
                return [idx, otherIdx]

        return [-1, -1]
