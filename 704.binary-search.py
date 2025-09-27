class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                # target is in right section
                left = mid + 1
            else:
                # target is in left section
                right = mid - 1

        return -1
