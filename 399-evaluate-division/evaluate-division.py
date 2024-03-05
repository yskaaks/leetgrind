class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def build_graph(equations, values):
            graph = collections.defaultdict(dict)
            for (a,b), value in zip(equations, values):
                graph[a][b] = value
                graph[b][a] = 1/value

            return graph
        
        def dfs(graph, start, end, visited):
            if start == end:
                return 1
            visited.add(start)
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    next_val = dfs(graph, neighbor, end, visited)

                    if next_val != -1:
                        return value * next_val
            return -1
        
        graph = build_graph(equations, values)
        res = []
        for start, end in queries:
            if start in graph and end in graph:
                res.append(dfs(graph, start, end, set()))
            else:
                res.append(-1)
        return res