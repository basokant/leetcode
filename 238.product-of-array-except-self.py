# @leet start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        products = [1] * len(nums)
        prefix_sum = [1] * len(nums)

        # suffix sum
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                continue

            products[i] = products[i + 1] * nums[i + 1]

        # prefix sum
        for i in range(len(nums)):
            if i == 0:
                continue

            prefix_sum[i] = prefix_sum[i - 1] * nums[i - 1]
            products[i] *= prefix_sum[i]

        return products


# @leet end
