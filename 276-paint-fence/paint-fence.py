class Solution:
    def numWays(self, n: int, k: int) -> int:
        memo = {}
        def dfs(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            if i in memo:
                return memo[i]
            memo[i] = (k-1) * (dfs(i-1) + dfs(i-2))
            return memo[i]
        return dfs(n)
