class Solution:
    # problems that could not be answered correctly
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            m = (r+l)//2

            if nums[m] == target:
                return m
            # 左側が昇順
            if nums[l] <= nums[m]:
                if (target > nums[m]) or (target < nums[l]):
                    l = m + 1
                else:
                    r = m - 1
            # 右側が昇順
            else:
                if (target < nums[m]) or (target > nums[r]):
                    r = m - 1
                else:
                    l = m + 1
        return -1


if __name__ == '__main__':
    print(Solution().search([4,5,6,7,0,1,2], 0))  # 4
