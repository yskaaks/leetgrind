class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        min_cost = [float("inf")] * len(points)
        min_cost[0] = 0
        min_heap = [(0,0)] # cost, point_index
        res = 0
        visited = set()

        while len(visited) < len(points):
            cost, index = heapq.heappop(min_heap)
            if index in visited:
                continue
            res += cost
            visited.add(index)
            
            for j in range(len(points)):
                if j not in visited:
                    new_cost = manhattan(points[index], points[j])

                    if new_cost < min_cost[j]:
                        min_cost[j] = new_cost
                        heapq.heappush(min_heap, (new_cost, j))
        return res


