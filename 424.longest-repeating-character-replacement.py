class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = dict[str, int]()
        res = 0
        maxf = 0

        for right in range(0, len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxf = max(maxf, count[s[right]])

            num_replacements = (right - left + 1) - maxf
            while num_replacements > k:
                count[s[left]] -= 1
                left += 1
                num_replacements = (right - left + 1) - maxf

            res = max(res, right - left + 1)

        return res
