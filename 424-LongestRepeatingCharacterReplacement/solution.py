class Solution:
    # Problems that could not be answered correctly
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


if __name__ == '__main__':
    print(Solution().characterReplacement("ABAB", 2))  # 4
    print(Solution().characterReplacement("AABABBA", 1))  # 4
