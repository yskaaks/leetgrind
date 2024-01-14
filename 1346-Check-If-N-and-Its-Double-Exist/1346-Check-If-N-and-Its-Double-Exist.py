class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # binary search nlogn
        arr.sort()
        for i in range(len(arr)):
            target = arr[i] * 2
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (right + left) // 2

                if arr[mid] == target and mid != i:
                    return True
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False        
        # naive approach n2
        # for i in range(len(arr)):
        #     target = arr[i] * 2
        #     for j in range(len(arr)):
        #         if arr[j] == target and i != j:
        #             return True
        # return False
