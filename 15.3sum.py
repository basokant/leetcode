class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        sorted_nums = sorted(nums)

        for i, num1 in enumerate(sorted_nums):
            if num1 > 0:
                break

            if i > 0 and num1 == sorted_nums[i - 1]:
                continue

            j, k = i + 1, len(sorted_nums) - 1

            while j < k:
                num2, num3 = sorted_nums[j], sorted_nums[k]
                threeSum = num1 + num2 + num3

                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    res.append([num1, num2, num3])
                    j += 1
                    k -= 1
                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1

        return res
