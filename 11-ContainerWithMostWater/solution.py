class Solution:
    # first solution(runtime: 578ms, memory: 30.38MB)
    def maxArea(self, height: list[int]) -> int:

        res = []
        l, r = 0, len(height) - 1

        while l < r:

            width = r - l

            if height[l] <= height[r]:
                area = height[l] * width
                l += 1
                res.append(area)
                continue

            if height[l] > height[r]:
                area = height[r] * width
                r -= 1
                res.append(area)
                continue
        return max(res)

    # second solution(runtime: 526ms, memory: 29.59MB)
    def maxArea2(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
