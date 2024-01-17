import collections


class Solution:

    # first solution(runtime: 46ms, memory: 18.12 MB)
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    # second solution(runtime: 48ms, memory: 17.87 MB)
    def isAnagram2(self, s: str, t: str) -> bool:

        seen = collections.defaultdict(int)

        for i in s:
            seen[i] += 1

        for i in t:
            seen[i] -= 1

        for k in seen.values():
            if k != 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isAnagram1("anagram", "nagaram"))  # True
    print(Solution().isAnagram1("rat", "car"))  # False
    print(Solution().isAnagram1("a", "ab"))  # False
