class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue

            b, a = stack.pop(), stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))

        return stack[0]
