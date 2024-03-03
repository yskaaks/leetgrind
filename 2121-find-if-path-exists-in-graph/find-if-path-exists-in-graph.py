class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_lst = collections.defaultdict(list)
        for src, dest in edges:
            adj_lst[src].append(dest)
            adj_lst[dest].append(src)
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            if node in visited:
                return False
            visited.add(node)
            for next_node in adj_lst[node]:
                if dfs(next_node):
                    return True
            return False
        return dfs(source)