class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dfs(index):
            if index >= len(s):
                return 1
            if s[index] == "0":
                return 0
            
            if index in memo:
                return memo[index]

            
            # option 1 take a single character
            res = dfs(index+1)
            
            # option 2 take 2 characters
            # so if the its 1 than second character can be any digit 
            # but if its 2 then second character has to be between 0-6
            if index + 1 < len(s) and (s[index] == "1" or (s[index] == "2" and s[index + 1] in "0123456")):
                res += dfs(index+2)
            memo[index] = res
            return memo[index]
        return dfs(0)