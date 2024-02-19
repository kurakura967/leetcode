class Solution:
    # first solution(runtime: 48 ms, memory: 16.86 MB)
    def findMin1(self, nums: list[int]) -> int:
        return min(nums)

    # second solution(runtime: 50 ms, memory: 16.91 MB)
    def findMin2(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (r + l) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res


if __name__ == '__main__':
    print(Solution().findMin2([3,4,5,1,2]))  # 1
