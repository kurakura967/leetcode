class Solution:
    def canJump(self, nums: list[int]) -> bool:

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            # 4 + 4 >= 4 -> 3 + 1 >= 4 -> 2 + 1 >= 3 -> 1 + 3 >= 3  -> 0 + 2 >= 2
            if i + nums[i] >= goal:
                goal = i  # 4 -> 3 -> 2 -> 1 -> 0

        return True if goal == 0 else False


if __name__ == '__main__':
    print(Solution().canJump([2,3,1,1,4]) == True)
    #print(Solution().canJump([3,2,1,0,4]) == False)
