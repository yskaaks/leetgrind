class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = collections.defaultdict(list)

        for src, dest, cost in times:
            adj_list[src].append((dest, cost))

        path_weight = {node: float("inf") for node in range(1, n+1)}
        path_weight[k] = 0

        min_heap = [(0, k)] # path_weight, node
        visited = set()

        while min_heap:
            curr_path_weight, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            visited.add(node)

            if curr_path_weight > path_weight[node]:
                continue
            for neighbour, time in adj_list[node]:
                if neighbour not in visited:
                    new_path_weight = curr_path_weight + time
                    if new_path_weight < path_weight[neighbour]:
                        path_weight[neighbour] = new_path_weight
                    
                    heapq.heappush(min_heap, (new_path_weight, neighbour))
        
        max_time = max(path_weight.values())
        return max_time if max_time != float("inf") else -1

        # def dfs(node, curr_time):
        #     if visited[node]:
        #         return
        #     visited[node] = True

        #     times[node] = min(times[node], curr_time)
        #     for neighbour, time in adj_list[node]:
        #         dfs(neighbour, time+curr_time)
        # dfs(k, 0)
        # max_time = max(times[1:])
        # return max_time if max_time != float("inf") else -1
