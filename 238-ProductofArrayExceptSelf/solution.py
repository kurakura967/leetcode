class Solution:

    # Problems that could not be answered correctly
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]
    print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
