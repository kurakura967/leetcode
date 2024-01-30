class Solution:
    # Problems that could not be answered correctly
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        stack = []  # [[temp, idx], ...]
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                stacked_temp, stacked_idx = stack.pop()
                ans[stacked_idx] = i - stacked_idx

            stack.append([t, i])
        return ans


if __name__ == '__main__':
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]
