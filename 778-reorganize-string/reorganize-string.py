from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        res = []
        max_heap = []
        for char, count in counter.items():
            max_heap.append((-count, char))
        heapq.heapify(max_heap)

        while max_heap:
            count, char = heapq.heappop(max_heap)
            if res and res[-1] == char:
                if not max_heap:
                    return ""
                count2, char2 = heapq.heappop(max_heap)
                res.append(char2)
                if count2 < -1:
                    heapq.heappush(max_heap, (count2 + 1, char2))
                heapq.heappush(max_heap, (count, char))
            else:
                res.append(char)
                if count < -1:
                    heapq.heappush(max_heap, (count + 1, char))

        return ''.join(res)
            

        # res = []
        # counter = Counter(s)
        # def backtrack(last_char, remaining_count):
        #     if not any(remaining_count.values()):
        #         return ''.join(res)
        #     for char, count in remaining_count.items():
        #         if char != last_char and count > 0:
        #             res.append(char)
        #             remaining_count[char] -= 1
        #             solution = backtrack(char, remaining_count)
        #             if solution:
        #                 return solution
        #             res.pop()
        #             remaining_count[char] += 1
        #     return ""
        # return backtrack("", counter)