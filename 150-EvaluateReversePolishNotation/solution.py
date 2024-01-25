class Solution:

    # first solution(runtime: 57 ms, memory: 17.13 MB)
    def evalRPN1(self, tokens: list[str]) -> int:

        operators = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:

            # 演算子ではない場合は数値をstackに後ろから追加する
            if token not in operators:
                stack.append(int(token))
                continue

            num1 = stack.pop()
            num2 = stack.pop()

            if token == "+":
                res = num1 + num2

            if token == "-":
                res = num2 - num1

            if token == "*":
                res = num1 * num2

            if token == "/":
                res = int(num2 / num1)

            stack.append(res)
        return stack.pop()

    # second solution(runtime: 66 ms, memory: 17.10MB)
    def evalRPN2(self, tokens: list[str]) -> int:
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        stack = []
        for token in tokens:

            if token not in "+-*/":
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()

            stack.append(operators[token](a, b))

        return stack.pop()


if __name__ == '__main__':
    print(Solution().evalRPN1(["2", "1", "+", "3", "*"]))  # 9
