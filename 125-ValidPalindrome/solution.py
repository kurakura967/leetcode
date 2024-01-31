import re

PATTERN = re.compile(r"[^a-z0-9]")


class Solution:
    # first solution(runtime: 44ms, memory: 18.01MB)
    def isPalindrome1(self, s: str) -> bool:
        string = PATTERN.sub("", s)
        lower_string = string.lower()

        reverse_string = lower_string[::-1]

        return lower_string == reverse_string

    # second solution(runtime: 39ms, memory: 16.94MB)
    def isPalindrome2(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r-1

        return True

    # third solution(runtime: 43ms, memory: 17.204MB)
    def isPalindrome3(self, s: str) -> bool:

        string = "".join([char for char in s if char.isalnum()])
        lower_string = string.lower()

        return lower_string == lower_string[::-1]


if __name__ == '__main__':
    print(Solution().isPalindrome2("A man, a plan, a canal: Panama"))  # True
