
class Solution:
    # problems that could not be answered correctly
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        ans = []
        nums.sort()
        for idx, num in enumerate(nums):

            if idx > 0 and num == nums[idx - 1]:
                continue
            l, r = idx + 1, len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    # 次の要素が同じ場合はチェックする必要がないのでスキップする
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return ans


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
