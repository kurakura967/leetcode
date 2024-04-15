class Solution:
    # Problem that could not be answered correctly
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        res = []
        nums.sort()

        def backtrack(i, subset):

            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)

        backtrack(0, [])
        return res


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1,2,2]) == [[],[1],[1,2],[1,2,2],[2],[2,2]])
