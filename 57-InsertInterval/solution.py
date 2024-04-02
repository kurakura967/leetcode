class Solution:
    # Problems that could not be answered correctly
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []

        for i in range(len(intervals)):

            # newIntervalの終点がintervals[i]の始点より小さい場合
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:] # -> [[1, 5], [6, 9]]

            # newIntervalの始点がintervals[i]の終点より大きい場合
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            else:
                # newIntervalとintervals[i]が重なっている場合
                # newIntervalとintervals[i]の両端(最小値, 最大値)を取得する
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])] # newInterval = [1, 5]

        res.append(newInterval)

        return res


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(Solution().insert(intervals, newInterval))  # [[1, 5], [6, 9]]
