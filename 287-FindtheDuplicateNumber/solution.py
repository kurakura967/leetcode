from collections import defaultdict

class Solution:
    # first solution(runtime: 36.36 ms, memory: 36.36 MB)
    def findDuplicate1(self, nums: list[int]) -> int:
        hash_map = defaultdict(int)

        for n in nums:

            if hash_map[n] > 0:
                return n

            hash_map[n] += 1

    # second solution(runtime: 531 ms, memory: 31.02 MB)
    def findDuplicate2(self, nums: list[int]) -> int:

        slow = nums[0] # 1
        fast = nums[0] # 1

        while True:
            slow = nums[slow] # 3 -> 2
            fast = nums[nums[fast]] # 2 -> 2

            if slow == fast:
                break

        slow = nums[0] # 1
        while slow != fast:
            print(slow, fast) # 1 2 -> 3 4
            slow = nums[slow] # 3 -> 2(slow != fastとなるのでwhileを抜ける)
            fast = nums[fast] # 4 -> 2(slow != fastとなるのでwhileを抜ける)
        return slow


if __name__ == '__main__':
    print(Solution().findDuplicate2([1, 3, 4, 2, 2]))  # 2
