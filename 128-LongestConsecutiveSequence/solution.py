
class Solution:
    # first solution(runtime: 429 ms, memory: 32.77 MB)
    def longestConsecutive1(self, nums: list[int]) -> int:
        res = []
        tmp = []
        before = None
        for num in sorted(set(nums)):
            if len(tmp) == 0:
                tmp.append(num)
                before = num
                continue

            diff = num - before
            if diff > 1:
                res.append(len(tmp))
                tmp = [num]
                before = num
                continue
            tmp.append(num)
            before = num

        res.append(len(tmp))
        return max(res)

    # second solution(runtime: 4397 ms, memory: 31.82 MB)
    def longestConsecutive2(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest


if __name__ == '__main__':
    print(Solution().longestConsecutive1([100, 4, 200, 1, 3, 2]))  # 4

