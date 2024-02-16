class Solution:
    # first solution(runtime: 49 ms, memory: 17.09 MB)
    def searchMatrix1(self, matrix: list[list[int]], target: int) -> bool:
        half = len(matrix) // 2
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid_row = matrix[half]
            if target in mid_row:
                return True
            min_num = mid_row[0]

            if target < min_num:
                r = half - 1
            else:
                l = half + 1

            half = (r + l) // 2

        return False

    # second solution(runtime: 50 ms, memory: 17.12 MB)
    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # どの行にあるかを二分探索する
        top, bottom = 0, rows - 1
        while top <= bottom:
            row = (top + bottom) // 2

            # 行の先頭の値よりも小さい場合
            if target < matrix[row][0]:
                bottom = row - 1

            # 行の最後の値よりも大きい場合
            elif target > matrix[row][-1]:
                top = row + 1

            # 行の先頭の値と最後の値の間にある場合
            else:
                # 該当のrowを動かす必要がない
                break

        if not (top <= bottom):
            return False

        # 該当の行の配列を二分探索する
        row = (top + bottom) // 2
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

    # third solution(runtime: 38 ms, memory: 17.14 MB)
    def searchMatrix3(self, matrix: list[list[int]], target: int) -> bool:

        # Brute Force(単純な線形探索)
        for row in matrix:
            if row[-1] >= target:
                return target in row
        return False


if __name__ == '__main__':
    print(Solution().searchMatrix1(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))  # True
