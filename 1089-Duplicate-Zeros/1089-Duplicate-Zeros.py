class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new = []
        for i in range(len(arr)):
            if arr[i] == 0:
                new.append(arr[i])
                new.append(0)
            else:
                new.append(arr[i])
    
        while len(new) > len(arr):
            new.pop()
        
        for i in range(len(new)):
            arr[i] = new[i]
        