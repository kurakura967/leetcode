class Solution:
    # Problem that could not be answered correctly
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n # 0 + (-2) = -2 -> 0 + 1 = 1 -> 1 + (-3) = -2 -> 0 + 4 = 4 -> 4 + (-1) = 3 -> 3 + 2 = 5 -> 5 + 1 = 6 -> 6 + (-5) = 1 -> 1 + 4 = 5
            max_sum = max(max_sum, cur_sum)
        return max_sum


if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
