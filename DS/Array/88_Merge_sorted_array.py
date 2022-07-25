class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ## Initial solution...
        # p1,p2 = 0,0 # progress in 1 and 2
        # temp = []
        
        # while not(p1==m and p2==n):
        #     if len(nums1) == 0:
        #         temp.append(nums2[p2])
        #         p2 += 1

        #     elif len(nums2) == 0:
        #         temp.append(nums1[p1])
        #         p1 += 1

        #     else:
        #         if p1<=m-1:
        #             if nums1[p1] < nums2[p2]:
        #                 temp.append(nums1[p1])
        #                 p1 += 1
                    
        #             if nums1[p1] > nums2[p2]:
        #                 temp.append(nums2[p2])
        #                 p2 += 1
            
        #             if nums1[p1] == nums2[p2]:
        #                 temp.append(nums1[p1])
        #                 temp.append(nums2[p2])
        #                 p1 += 1
        #                 p2 += 1
                
        #             temp.append(nums1[p1])
        #             p1 +=1
                    
        #         elif p2<=n-1:
        #             temp.append(nums2[p2])
        #             p2 += 1

        #         else: break
        # del(nums1)
        # nums1 = temp
        # print(nums1)

        # Much easier solution... # Credits to Teslavolt on leetcode.com 
        nums1[m:] = nums2[:n]
        nums1.sort()

sol = Solution()
sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
sol.merge(nums1 = [1], m = 1, nums2 = [], n = 0)
sol.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)