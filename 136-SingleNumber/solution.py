from collections import Counter


class Solution:
    # first solution(runtime: 117 ms, memory: 19.28 MB)
    def singleNumber1(self, nums: list[int]) -> int:

        counter = Counter(nums)

        for k, v in counter.items():
            if v == 1:
                return k

    # second solution(runtime: 112 ms, memory: 19.15 MB)
    def singleNumber2(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
            print(res)
        return res


if __name__ == '__main__':
    print(Solution().singleNumber2([2,2,1]) == 1)
