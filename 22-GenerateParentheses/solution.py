class Solution:
    # Problems that could not be answered correctly
    def generateParenthesis(self, n: int) -> list[str]:

        stack = []
        res = []

        def backtrack(open_n, closed_n):
            print(stack)
            if open_n == closed_n == n:
                res.append(''.join(stack))
                return

            if open_n < n:
                stack.append('(')
                backtrack(open_n + 1, closed_n)
                stack.pop()

            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n+1)
                stack.pop()

        backtrack(0, 0)
        return res


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
