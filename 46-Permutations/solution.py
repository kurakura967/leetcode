class Solution:
    # first solution(runtime: 50 ms, memory: 16.70 MB)
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(stack):

            if len(set(stack)) == len(nums):

                res.append(stack.copy())
                return

            for i in range(len(nums)):
                if nums[i] in stack:
                    continue
                stack.append(nums[i])
                backtrack(stack)
                stack.pop()

        backtrack([])
        return res


if __name__ == '__main__':
    Solution().permute([1,2,3])
