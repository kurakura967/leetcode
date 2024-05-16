class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_aria = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_aria = max(max_aria, self.dfs(grid, i, j))
        return max_aria

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0

        grid[i][j] = 0
        count = 1

        count += self.dfs(grid, i, j+1)
        count += self.dfs(grid, i, j-1)
        count += self.dfs(grid, i+1, j)
        count += self.dfs(grid, i-1, j)

        return count


if __name__ == '__main__':
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    print(Solution().maxAreaOfIsland(grid=grid))
