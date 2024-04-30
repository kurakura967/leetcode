class Solution:
    # first solution(runtime: 30 ms, memory: 16.59 MB)
    def uniquePaths1(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        # 1行または1列しかない場合、1通りしかない
        if m < 2 or n < 2:
            return 1

        dp[1][2] = 1
        dp[2][1] = 1

        for row in range(1, m + 1):
            for column in range(1, n + 1):

                dp[row][column] += dp[row - 1][column] + dp[row][column - 1]
        print(dp)
        return dp[-1][-1]


    def uniquePaths2(self, m: int, n: int) -> int:

        row = [1] * n

        for i in range(m - 1):
            new_row = [1] * n
            for j in range(n-2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row
        return row[0]

    # second solution(runtime: 41 ms, memory: 16.46 MB)
    def uniquePaths3(self, m: int, n: int) -> int:

        dp = [[1 for j in range(n)] for i in range(m)]
        # 1行または1列から処理を始めると0行目と0列目の1通りのマス目を処理する必要がない
        for i in range(1, m):
            for j in range(1, n):

                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        print(dp)
        return dp[m-1][n-1]


if __name__ == '__main__':
    print(Solution().uniquePaths1(3, 7) == 28)
     # [[0, 0, 0, 0, 0, 0, 0, 0],
     # [0, 0, 1, 1, 1, 1, 1, 1],
     # [0, 1, 2, 3, 4, 5, 6, 7],
     # [0, 1, 3, 6, 10, 15, 21, 28]]

    print(Solution().uniquePaths3(3, 7) == 28)
    # [[1, 1, 1, 1, 1, 1, 1],
    # [1, 2, 3, 4, 5, 6, 7],
    # [1, 3, 6, 10, 15, 21, 28]]
