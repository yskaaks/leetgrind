class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        adj_list = collections.defaultdict(list)
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nxt in adj_list[node]:
                dfs(nxt)
        
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count