class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} # key=(day, transactions, holding), value=profit
        # state = 0 means, holding the stock ready to sell
        # state = 1 means, sold the stock ready to buy
        def dfs(index, transactions, state):
            if index >= len(prices) or transactions == 2:
                return 0
            if (index, transactions, state) in memo:
                return memo[(index,transactions, state)]
            if state == 0: # holding the stock
                # can either sell or skip
                sell = dfs(index+1, transactions + 1, 1) + prices[index]
                skip = dfs(index+1, transactions, 0)
                memo[(index,transactions, state)] = max(sell, skip)
            elif state == 1: # can buy or skip
                buy = dfs(index+1, transactions, 0) - prices[index]
                skip = dfs(index+1,transactions, 1)
                memo[(index,transactions, state)] = max(buy, skip)
            return memo[(index,transactions, state)]
        return dfs(0, 0, 1)


            
