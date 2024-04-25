class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        memo = {}
        dp = [0] * 26
        for char in s:
            curr = ord(char) - ord('a')
            longest = 1
            for prev in range(26):
                if abs(curr - prev) <= k:
                    longest = max(longest, 1+dp[prev])
            dp[curr] = max(dp[curr], longest)
        return max(dp)
        # def dfs(i, prev):
        #     if i == len(s):
        #         return 0
        #     if (i, prev) in memo:
        #         return memo[(i, prev)]
        #     # skip s[i]
        #     res = dfs(i+1, prev)

        #     # include s[i]
        #     if prev == "" or abs(ord(s[i]) - ord(prev)) <= k:
        #         res = max(res, 1+ dfs(i+1, s[i]))
        #     memo[(i, prev)] = res
        #     return res
        # return dfs(0, "")