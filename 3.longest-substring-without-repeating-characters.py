class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        charSet = set()

        res = 0

        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            res = max(res, right - left + 1)
            charSet.add(s[right])
            right += 1

        return res
