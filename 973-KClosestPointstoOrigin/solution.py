import math
import heapq


class Solution:
    # first solution(runtime: 626 ms, memory: 22.29 MB)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        stack = []

        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(stack, (distance, point))

        return [heapq.heappop(stack)[1] for _ in range(k)]


if __name__ == '__main__':
    print(Solution().kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]])
