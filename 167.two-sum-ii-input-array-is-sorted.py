# @leet start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                break

            if sum < target:
                left += 1
            elif sum > target:
                right -= 1

        return [left + 1, right + 1]


# @leet end
