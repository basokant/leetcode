class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = "".join(c for c in list(s) if c.isalnum()).lower()
        left, right = 0, len(alpha_s) - 1

        while left < right:
            if alpha_s[left] != alpha_s[right]:
                return False

            left += 1
            right -= 1

        return True
