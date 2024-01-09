class Solution:
    # first solution(runtime: 46ms, memory: 17.3MB)
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    print(Solution().isPalindrome(121))  # True
    print(Solution().isPalindrome(-121))  # False

