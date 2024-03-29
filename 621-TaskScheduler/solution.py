import heapq
from collections import Counter, deque

class Solution:
    # Problem that could not be answered correctly
    def leastInterval(self, tasks: list[str], n: int) -> int:

        count = Counter(tasks)
        max_heap = [-val for val in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()

        while max_heap or q:

            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time


if __name__ == '__main__':
    print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8)
