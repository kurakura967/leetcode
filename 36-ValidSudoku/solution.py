import numpy as np
from collections import defaultdict


class Solution:

    # first solution(runtime: 189 ms, memory: 36.79 MB)
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        board = np.array(board)
        for i in range(0, len(board), 3):
            for j in range(len(board), 0, -3):
                three_by_three = board[i:i+3, j-3:j]
                flatten = three_by_three.flatten()
                seen = defaultdict(int)
                for c in flatten:
                    if c == ".":
                        continue
                    if seen[c] > 0:
                        return False
                    seen[c] += 1

        for i in range(len(board)):
            col = board[:, i]
            seen = defaultdict(int)

            for c in col:
                if c == ".":
                    continue

                if seen[c] > 0:
                    return False
                seen[c] += 1

        for i in range(len(board)):
            row = board[i]
            seen = defaultdict(int)

            for c in row:
                if c == ".":
                    continue

                if seen[c] > 0:
                    return False
                seen[c] += 1

        return True

    # second solution(runtime: 160 ms, memory: 36.85 MB)
    def isValidSudoku2(self, board: list[list[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                if (
                        board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r//3, c//3)]
                ):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True


if __name__ == '__main__':
    print(Solution().isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))

