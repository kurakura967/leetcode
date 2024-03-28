import heapq


class Solution:
    # first solution(runtime: 510 ms, memory: 28.58 MB)
    def findKthLargest(self, nums: list[int], k: int) -> int:

        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]


if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
