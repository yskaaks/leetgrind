class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)

        for prev_crs, next_crs in relations:
            adj_list[prev_crs].append(next_crs)
        
        visited = set()
        being_visited = set()
        longest_path = {}
        def dfs(node):
            if node in being_visited:
                return -1
            if node in visited:
                return longest_path[node]
            being_visited.add(node)
            max_len = 0

            for neighbor in adj_list[node]:
                length = dfs(neighbor)
                if length == -1:
                    return -1
                max_len = max(max_len, length)            
            being_visited.remove(node)
            visited.add(node)
            longest_path[node] = 1 + max_len
            return longest_path[node]
        
        for i in range(1, n+1):
            if dfs(i) == -1:
                return -1
        return max(longest_path.values())
