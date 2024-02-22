class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}

        for i in range(2, n + 1):
            val = 0
            for j in range(1, i):
                val = max(val, max(dp[j], j) * max(i-j, dp[i-j]))
            dp[i] = val
        return dp[n]

        
        # memo = {1:1}

        # def dfs(num):
        #     if num in memo:
        #         return memo[num]
        #     memo[num] = 0 if num == n else num
        #     for i in range(1, num):
        #         val = dfs(i) * dfs(num - i)
        #         memo[num] = max(memo[num], val)
        #     return memo[num]
        # return dfs(n)




        # if n == 2:
        #     return 1
        # if n == 3:
        #     return 2
        # if n % 3 == 0:
        #     return 3 ** (n // 3)
        # if n % 3 == 1:
        #     return 3 ** (n // 3 - 1) * 4
        # return 3 ** (n // 3) * 2