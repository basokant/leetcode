class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < nums[(mid - 1) % len(nums)]:
                return nums[mid]
            elif nums[left] < nums[right] or nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return nums[right]
