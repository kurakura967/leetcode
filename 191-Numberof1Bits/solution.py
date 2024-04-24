class Solution:
    # Problem that could not be answered correctly
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res


if __name__ == '__main__':
    print(Solution().hammingWeight(2147483645) == 30)
