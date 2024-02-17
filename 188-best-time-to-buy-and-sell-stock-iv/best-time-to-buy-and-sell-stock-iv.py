class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {} # key = (day, transaction, state), val = profit
        
        def dfs(index, transaction, state):
            if index >= len(prices) or transaction == k:
                return 0
            if (index, transaction, state) in memo:
                return memo[(index, transaction, state)]
            if state == 0: # holding the stock
                sell = dfs(index + 1, transaction + 1, 1) + prices[index]
                skip = dfs(index+1, transaction, 0)
                memo[(index, transaction, state)] = max(sell, skip)
            elif state == 1: # not holding the stock
                buy = dfs(index+1, transaction, 0) - prices[index]
                skip = dfs(index+1, transaction, 1)
                memo[(index, transaction, state)] = max(buy, skip)
            return memo[(index, transaction, state)]
        return dfs(0, 0, 1)