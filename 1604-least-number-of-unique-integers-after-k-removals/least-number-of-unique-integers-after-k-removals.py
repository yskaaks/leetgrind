class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        freq_list = [0] * (len(arr) + 1) # each index represents frequency so 
        #if index 1 value is 2 means there are 2 elemtns in arr with freq of 1

        for num, freq in counter.items():
            freq_list[freq] += 1
        res = len(counter)
        for f in range(1, len(freq_list)):
            remove = freq_list[f] 
            if k >= remove * f:
                k -= remove * f
                res -= remove
            else:
                remove = k // f
                res -= remove
                break
        return res


        # heap = []

        # for num, freq in counter.items():
        #     heapq.heappush(heap, (freq, num))


        # while k > 0 and heap:
        #     freq, num = heapq.heappop(heap)
        #     if k >= freq:
        #         k -= freq
        #     else:
        #         heapq.heappush(heap, (freq - k, num))
        #         k = 0  # All k removals used up
        # return len(heap)