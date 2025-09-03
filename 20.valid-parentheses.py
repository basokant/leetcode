class Solution:
    def isValid(self, s: str) -> bool:
        match_dict = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for c in s:
            if c in match_dict.values():
                stack.append(c)
                continue

            if c in match_dict.keys() and not stack or stack.pop() != match_dict[c]:
                return False

        if stack:
            return False

        return True
