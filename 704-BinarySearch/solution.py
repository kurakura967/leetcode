class Solution:

    # first solution(runtime: 185 ms, memory: 18.19 MB)
    def search(self, nums: list[int], target: int) -> int:

        half = len(nums) // 2
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[half] == target:
                return half

            elif nums[half] < target:
                l = half + 1
            else:
                r = half - 1

            half = (r + l) // 2
        return -1


if __name__ == '__main__':

    print(Solution().search([-1,0,3,5,9,12], 9))  # 4
