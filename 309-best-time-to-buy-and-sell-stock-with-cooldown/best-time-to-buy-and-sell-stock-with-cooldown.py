class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} # key=(index, state) val=maxprofit
        # state = 0: holding, ready to sell
        # state = 1: just sold, must cooldown
        # state = 2: no stock, can buy or cooldown
        def dfs(index, state):
            if index >= len(prices):
                return 0
            if (index, state) in memo:
                return memo[(index, state)]
            if state == 0: # holdin, ready to sell
                # choice are: sell or cooldown
                sell = dfs(index+1, 1) + prices[index] # sell the stock
                cooldown = dfs(index+1, 0) # hold the stock, no transaction
                memo[(index, state)] = max(sell, cooldown)
            elif state == 1: # just sold, must cooldown
                # the only choice is forced cooldown
                cooldown = dfs(index+1, 2)
                memo[(index, state)] = cooldown
            else: # not holding anything
                # choices are either buy or cooldown
                buy = dfs(index+1, 0) - prices[index]
                cooldown = dfs(index+1, 2)
                memo[(index, state)] = max(buy, cooldown)
            return memo[(index, state)]
        # start with day 0, state should be not holding anything so either buy or cooldown
        return dfs(0, 2)