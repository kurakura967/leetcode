class Solution:
    # first solution(runtime: 126 ms, memory: 20.49 MB)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = []
        intervals.sort(key=lambda i: i[0])
        new_interval = intervals[0]
        tmp_intervals = intervals[1:]

        for i in range(len(tmp_intervals)):
            # new_intervalsの終点がintervals[i]の始点よりも小さい場合
            if new_interval[1] < tmp_intervals[i][0]:
                res.append(new_interval)
                new_interval = tmp_intervals[i]
                continue

            else:
                new_interval = [min(new_interval[0], tmp_intervals[i][0]), max(new_interval[1], tmp_intervals[i][1])]
        res.append(new_interval)
        return res

    # second solution(runtime: 127 ms, memory: 21.01 MB)
    def merge2(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        output = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = output[-1][1]

            # 次の要素の始点が前の要素の終点よりも小さい場合
            # ex) [1,3], [2, 6]
            if start <= last_end:
                output[-1][1] = max(last_end, end)  # [1, 6]
            else:
                output.append([start, end])
        return output


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge2(intervals))  # [[1, 6], [8, 10], [15, 18]]
