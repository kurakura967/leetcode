class Solution:

    # Problems that could not be answered correctly
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start_idx = i
            while stack and stack[-1][1] > h:
                stacked_idx, stacked_h = stack.pop()
                max_area = max(max_area, stacked_h * (i - stacked_idx))
                start_idx = stacked_idx
            stack.append([start_idx, h])

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area


if __name__ == '__main__':
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))   # 10
