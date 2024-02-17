class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        dp = [0] * (len(s)+1)
        dp[0], dp[1] = 1, 1
        
        for i in range(2, len(s) + 1):
            # single digit case if its not 0
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
        return dp[-1]
                
        
        
#         memo = {}
        
#         def dfs(index):
#             if index >= len(s):
#                 return 1
#             if s[index] == "0":
#                 return 0
            
#             if index in memo:
#                 return memo[index]

            
#             # option 1 take a single character
#             res = dfs(index+1)
            
#             # option 2 take 2 characters
#             # so if the its 1 than second character can be any digit 
#             # but if its 2 then second character has to be between 0-6
#             if index + 1 < len(s) and (s[index] == "1" or (s[index] == "2" and s[index + 1] in "0123456")):
#                 res += dfs(index+2)
#             memo[index] = res
#             return memo[index]
#         return dfs(0)