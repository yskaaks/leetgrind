class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # two pointer
        lst = []
        for i in nums:
            lst.append(i**2)
        res = []
        left, right = 0, len(lst) - 1
        while left <= right:
            if lst[left] > lst[right]:
                res.append(lst[left])
                left += 1
            else:
                res.append(lst[right])
                right -= 1
        return res[::-1]
            


        # simple approach but nlogn time complexity
        # lst = []
        # for i in nums:
        #     lst.append(i**2)
        # lst.sort()
        # return lst