class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = collections.defaultdict(list)
        for s, d, cost in flights:
            adj_list[s].append((d, cost))

        heap = [(0, src, 0)] # cost, city, stops
        # key is (city, stops), value is cost
        memo = {(src, 0): 0}

        while heap:
            cost_so_far, city, stops = heapq.heappop(heap)

            # Check if the current city is the destination
            if city == dst:
                return cost_so_far

            if stops <= k:
                for nei, cost in adj_list[city]:
                    new_cost = cost + cost_so_far
                    if (nei, stops + 1) not in memo or new_cost < memo[(nei, stops+1)]:
                        memo[(nei, stops+1)] = new_cost
                        heapq.heappush(heap, (new_cost, nei, stops + 1))

        return -1