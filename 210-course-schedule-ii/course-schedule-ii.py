class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)

        for src, dst in prerequisites:
            adj_list[src].append(dst)
        res = []
        visited = set()  # Tracks all ever visited nodes
        being_visited = set()  # Tracks nodes being visited in current DFS path

        def dfs(curr_node):
            if curr_node in being_visited: # detected cycle 
                return False
            if curr_node in visited:
                return True
            being_visited.add(curr_node)

            for neighbour in adj_list[curr_node]:
                if not dfs(neighbour):
                    return False
            being_visited.remove(curr_node)
            visited.add(curr_node)
            res.append(curr_node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        
