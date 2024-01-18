from collections import defaultdict


class Solution:
    # first solution(runtime: 82 ms, memory: 21.69 MB)
    def topKFrequent1(self, nums: list[int], k: int) -> list[int]:
        map = defaultdict(int)

        for n in nums:

            map[n] += 1

        sorted_map = sorted(map, key=map.get, reverse=True)[:k]

        return sorted_map

    # second solution(runtime: 83 ms, memory: 21.91 MB)
    def topKFrequent2(self, nums: list[int], k: int) -> list[int]:

        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1

        for n, cnt in count.items():
            freq[cnt].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == '__main__':
    print(Solution().topKFrequent1([1, 1, 1, 2, 2, 3], 2))  # [1,2]
    print(Solution().topKFrequent1([1], 1))  # [1]
