class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
    
        left, right = 0, len(arr) - 1
        while left < right and arr[left] < arr[left + 1]:
                left += 1
        while left < right and arr[right] < arr[right - 1]:
                right -= 1
        if left == 0 or right == len(arr) - 1:
            return False
        return left == right