class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < nums[(mid - 1) % len(nums)]:
                return mid
            elif nums[left] < nums[right] or nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return right

    def search(self, nums: list[int], target: int) -> int:
        mini = self.findMin(nums)
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            rotated_mid = (mini + mid) % len(nums)

            if nums[rotated_mid] == target:
                return rotated_mid
            elif target < nums[rotated_mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1
