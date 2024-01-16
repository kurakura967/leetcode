class Solution:

    # first solution(runtime: 433 ms, memory: 32.75 MB)
    def containsDuplicate1(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

    # second solution(runtime: 436 ms, memory: 32.75 MB)
    def containsDuplicate2(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == '__main__':
    print(Solution().containsDuplicate1([1, 2, 3, 1]))  # True
    print(Solution().containsDuplicate1([1, 2, 3, 4]))  # False
