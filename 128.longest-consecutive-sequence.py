# @leet start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_len = 0
        nums_set = set(nums)

        for num in nums_set:
            is_start_of_seq = num - 1 not in nums_set
            if not is_start_of_seq:
                continue

            curr, curr_len = num + 1, 1
            while curr in nums_set:
                curr_len += 1
                curr += 1

            max_len = max(curr_len, max_len)

        return max_len


# @leet end

