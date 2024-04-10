class Solution:
    # Problem that could not be answered correctly
    def subsets(self, nums: list[int]) -> list[list[int]]:
        stack = []
        res = []

        def backtrack(i):

            if i >= len(nums):
                res.append(stack.copy()) # [1, 2, 3] -> [1, 2] // [1, 3] -> [1]
                return

            stack.append(nums[i]) # [1] -> [1, 2] -> [1, 2, 3] // [1, 3]
            backtrack(i+1) # backtrack(1) -> backtrack(2) -> backtrack(3) // backtrack(3) //

            stack.pop() # [1, 2] -> [1] -> [1]


            backtrack(i+1) # backtrack(3) -> backtack(2) -> backtrack(1)
        backtrack(0)
        return res

if __name__ == '__main__':
    print(Solution().subsets([1,2,3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
