class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        d = collections.defaultdict(int)

        for task in tasks:
            d[task] += 1
        
        heap = []
        for char, count in d.items():
            heapq.heappush(heap, (-count, char))
        
        time = 0
        while heap:
            i, temp = 0, []
            while i <= n:
                if heap:
                    count, task = heapq.heappop(heap)

                    if count < -1:
                        temp.append((count + 1, task))
                time += 1
                if not heap and not temp:
                    break
                i += 1
            for item in temp:
                heapq.heappush(heap, item)
        return time










        # if n == 0:
        #     return len(tasks)
        # d = {}
        # for i in tasks:
        #     if i not in d:
        #         d[i] = 0
        #     d[i] += 1

        # heap = []
        # for i in d.values():
        #     heapq.heappush(heap, -i)
        # time = 0
        # q = collections.deque() # (-count, idletime)

        # while heap or q:
        #     time += 1

        #     if heap:
        #         count = 1 + heapq.heappop(heap)
        #         if count:
        #             q.append([count, time + n])
            
        #     if q and q[0][1] == time:
        #         heapq.heappush(heap, q.popleft()[0])
            
        # return time