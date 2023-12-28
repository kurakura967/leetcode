class Solution:
    # first solution(runtime: 7817ms, memory: 18MB)
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for key_idx, key_value in enumerate(nums):

            for idx, value in enumerate(nums):

                if key_idx != idx and key_value + value == target:
                    return [key_idx, idx]
        return []

    # best solution(runtime: 62ms, memory: 18.7MB)
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for idx, value in enumerate(nums):

            remaining = target - value
            if remaining in seen:
                return [seen[remaining], idx]

            seen[value] = idx
        return []


if __name__ == '__main__':
    solution = Solution()

    print(solution.twoSum2([2, 7, 11, 15], 9))
    print(solution.twoSum2([2, 7, 11, 15], 13))  # [0,2]
    print(solution.twoSum2([3, 2, 4], 6))  # [1,2]
    print(solution.twoSum2([3, 3], 6))
