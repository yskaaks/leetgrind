class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = 0, 0
        s = set()
        nums1.sort()
        nums2.sort()
        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] == nums2[n2]:
                s.add(nums1[n1])
                n1 += 1
                n2 += 1
            elif nums1[n1] < nums2[n2]:
                n1 += 1
            else:
                n2 += 1
        return s