class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_idx = m + n - 1

        #merge in reverse order

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last_idx] = nums1[m-1]
                m -= 1
            else:
                nums1[last_idx] = nums2[n-1]
                n -= 1
            last_idx -= 1
        
        # fill nums1 with num2 leftovers

        while n > 0:
            nums1[last_idx] = nums2[n-1]
            n -= 1
            last_idx -= 1
        # naive approach
        # for i in range(n):
        #     nums1[i+m] = nums2[i]
        
        # nums1.sort()