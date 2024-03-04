class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(node, cur_path):
            cur_path.append(node)
            if node == len(graph) - 1:
                res.append(cur_path.copy())
            else:
                for next_node in graph[node]:
                    dfs(next_node, cur_path)
                    cur_path.pop()
        dfs(0, [])
        return res