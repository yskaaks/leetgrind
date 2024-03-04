class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor, is_connected in enumerate(isConnected[node]):
                if is_connected and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
            
        visited = set()
        res = 0
        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                res += 1
        return res
        