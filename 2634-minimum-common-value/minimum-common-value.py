class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1, n2 = 0, 0
        minn = float("inf")
        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] == nums2[n2]:
                return nums1[n1]
            elif nums1[n1] < nums2[n2]:
                n1 += 1
            else:
                n2 += 1
            
        return -1
        # min_element = float("inf")
        # n1 = {}
        # n2 = {}
        # for num in nums1:
        #     if num not in n1:
        #         n1[num] = 0
        #     n1[num] += 1
        
        # for num in nums2:
        #     if num not in n2:
        #         n2[num] = 0
        #     n2[num] += 1