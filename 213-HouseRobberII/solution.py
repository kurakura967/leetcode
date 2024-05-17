class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob
        return rob2


if __name__ == '__main__':
    print(Solution().rob([2,3,2]) == 3)
    print(Solution().rob([1,2,3,1]) == 4)
    print(Solution().rob([0]) == 0)
    print(Solution().rob([1]) == 1)
