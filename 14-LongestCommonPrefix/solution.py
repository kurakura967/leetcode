class Solution:

    # first solution(runtime: 32 ms, memory: 17.26 MB)
    def longestCommonPrefix(self, strs: list[str]) -> str:

        min_str = min(strs, key=len)

        for idx, w in enumerate(min_str):
            for s in strs:
                if s[idx] != w:
                    return min_str[:idx]
        return min_str


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))  # ""
