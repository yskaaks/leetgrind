class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)

        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        
        subtree_size = [0] * n
        subtree_sum_dist = [0] * n
        answer = [0] * n

        def dfs(node, parent):
            subtree_size[node] = 1
            for child in adj_list[node]:
                if child != parent:
                    dfs(child, node)
                    subtree_size[node] += subtree_size[child]
                    subtree_sum_dist[node] += subtree_sum_dist[child] + subtree_size[child]

        def dfs_update(node, parent):
            if parent != -1:
                answer[node] = answer[parent] - subtree_size[node] + (n - subtree_size[node])
            for child in adj_list[node]:
                if child != parent:
                    dfs_update(child, node)

        dfs(0, -1)
        answer[0] = subtree_sum_dist[0]
        dfs_update(0, -1)

        return answer