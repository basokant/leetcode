class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        temp_stack = []

        # maintain monotonically decreasing order stack
        for i, temp in enumerate(temperatures):
            while temp_stack and temp > temperatures[temp_stack[-1]]:
                j = temp_stack.pop()
                res[j] = i - j
            temp_stack.append(i)

        return res
