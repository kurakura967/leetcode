class Solution:
    # Problem that could not be answered correctly
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        cnt = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:

            # 次の要素の始点が前の要素の終点よりも大きい場合
            if start >= prev_end:
                prev_end = end
            else:
                cnt += 1
                prev_end = min(prev_end, end)
        return cnt


if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1)
