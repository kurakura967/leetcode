class Solution:
    # Problem that could not be answered correctly
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])
            cur.pop()
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res

if __name__ == '__main__':
    print(Solution().combinationSum([2,3,6,7], 7) == [[2,2,3],[7]])
