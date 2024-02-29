class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # recursive soluition
        return self.helper(0, nums)
    def helper(self, i, nums):
        if i == len(nums):
            return [[]]
        res_perms = []
        perms = self.helper(i+1, nums)

        for p in perms:
            for j in range(len(p) + 1):
                copy = p.copy()
                copy.insert(j, nums[i])
                res_perms.append(copy)
        return res_perms




    #    # iterative solution
    #     # initialize perms
    #     perms = [[]]

    #     # going through each number in nums
    #     for n in nums:
    #         next_perms = []
    #         for p in perms:
    #             # its len(p) + 1 because we need to add the number in the beginning, mid and end
    #             # so for example if the perms is [[4]], len(p) + 1 = 1 + 1 = 2, so we a num for example 2
    #             # to the beginning and the end ie [[2,4], [4,2]]
    #             for i in range(len(p) + 1):
    #                 # so we copy the [4]
    #                 copy = p.copy()
    #                 # within copy we insert [2,4] for the first iteation and second iteration we insert [4,2]
    #                 copy.insert(i, n)
    #                 # append these permutations to next_perm
    #                 next_perms.append(copy)
    #             # next_perms here will look like [[2,4], [4,2]] so we set it equal to the final perms and keep going
    #         perms = next_perms
    #     return perms
