import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums

        self.mim_heap = nums
        # ヒープキューを作成
        heapq.heapify(self.mim_heap)
        # キューの中でk番目に大きい要素を取得するので、k番目より小さい要素は削除する
        while len(self.mim_heap) > k:
            heapq.heappop(self.mim_heap)

    # time limit exceeded
    def add1(self, val: int) -> int:
        self.nums.append(val)
        return sorted(self.nums)[-self.k]

    # first solution(runtime: 87 ms, memory: 20.54 MB)
    def add2(self, val: int) -> int:
        # キューに要素を追加
        heapq.heappush(self.mim_heap, val)
        # キューの中でk番目に大きい要素を取得するので、k番目より小さい要素は削除する
        if len(self.mim_heap) > self.k:
            heapq.heappop(self.mim_heap)
        return self.mim_heap[0]


if __name__ == '__main__':
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add2(3)) # 4
    print(kthLargest.add2(5)) # 5
    print(kthLargest.add2(10)) # 5
    print(kthLargest.add2(9)) # 8
    print(kthLargest.add2(4)) # 8
