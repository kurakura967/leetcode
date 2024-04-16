class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def backtrack(i, cur, target):

            if target == 0:
                res.append(cur.copy())
                return

            if target <= 0:
                return

            prev = -1

            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                cur.append(candidates[j])
                backtrack(j + 1, cur, target - candidates[j])
                cur.pop()
                prev = candidates[j]

        backtrack(0, [], target)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum2([10,1,2,7,6,1,5], 8) == [[1,1,6],[1,2,5],[1,7],[2,6]])
