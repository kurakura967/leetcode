class Solution:
    # Problem that could not be answered correctly
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


if __name__ == '__main__':
    print(Solution().rob([1,2,3,1]) == 4)
