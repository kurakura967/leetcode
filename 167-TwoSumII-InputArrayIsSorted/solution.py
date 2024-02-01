class Solution:

    # first solution(runtime: 3586ms, memory: 17.58MB)
    def twoSum1(self, numbers: list[int], target: int) -> list[int]:

        for i, num in enumerate(numbers):
            res = target - num

            if res not in numbers[i+1:]:
                continue

            for j in range(len(numbers), 0, -1):
                if res == numbers[j-1]:
                    return [i+1, j]
        return []

    # second solution(runtime: 104ms, memory: 17.48MB)
    def twoSum2(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []


if __name__ == '__main__':
    print(Solution().twoSum2([2, 7, 11, 15], 9))  # [1, 2]
    print(Solution().twoSum2([2, 3, 4], 6))  # [1, 3]
    print(Solution().twoSum2([-1, 0], -1))  # [1, 2]

