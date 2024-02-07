class Solution:
    # first solution(runtime: 774ms, memory: 27.37MB)
    def maxProfit1(self, prices: list[int]) -> int:

        current_max_profit = 0
        current_min_price = prices[0]
        for idx in range(1, len(prices)):
            current_min_price = min(prices[idx-1], current_min_price)
            profit = prices[idx] - current_min_price

            if profit > current_max_profit:
                current_max_profit = profit

        return current_max_profit

    # second solution(runtime: 796ms, memory: 27.46MB)
    def maxProfit2(self, prices: list[int]) -> int:

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit1([7, 1, 5, 3, 6, 4]))  # 5
