import heapq


class Solution:
    # first solution(runtime: 37 ms, memory: 16.39 MB)
    def lastStoneWeight(self, stones: list[int]) -> int:

        reversed_stones = [-stone for stone in stones]
        heapq.heapify(reversed_stones)

        while len(reversed_stones) > 1:
            x = -1 * heapq.heappop(reversed_stones)
            y = -1 * heapq.heappop(reversed_stones)

            if x != y:
                heapq.heappush(reversed_stones, -abs(x - y))

        return -1 * reversed_stones[0] if reversed_stones else 0


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeight(stones))  # 1
