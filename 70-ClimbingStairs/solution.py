class Solution:
    # time limit exceeded
    def climbStairs(self, n: int) -> int:

        if n < 0:
            return 0
        elif n == 0:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs2(self, n: int) -> int:

        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one

    def climbStairs3(self, n: int) -> int:

        if n == 0 or n == 1:
            return 1

        dp = [0] * (n + 1)  # [0, 0, 0]
        dp[0], dp[1] = 1, 1 # [1, 1, 0]

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]  # [1] + [1] = [1,1,2]

        return dp[n]


if __name__ == '__main__':
    print(Solution().climbStairs3(2) == 2)
