class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
                
        # --- Below was too slow ---
        # Solution 1: for each index in array
        #     check if zero
        #          check if next not zero
        #          swap
                
        #         if zero, check 2 further

        # f = 0 # pointer moving through array once
        # b = 0 # offset for checking further elements

        # while f<len(nums)-1:
        #     if nums[f] == 0:
        #         if nums[f+b] != 0:
        #             nums[f] = nums[f+b]
        #             nums[f+b] = 0

        #             f += 1 
        #             b = 0 
        #         else:
        #             if (f+b) < len(nums)-1:
        #                 b += 1
        #             else: 
        #                 break
        #     else: 
        #         f += 1
        # --------------------------

        # Solution 2: rewrite to check for not zero instead
        
        b = 0 # tracks the index of where the non-zero value is supposed to end up (simple counter)

        for f in range(len(nums)):
            if nums[f] != 0:
                nums[f],nums[b] = nums[b],nums[f] # place the non-zero value at the at the available index
                b += 1
        print(nums)

sol = Solution()
sol.moveZeroes(nums = [0,1,0,3,12])
sol.moveZeroes(nums=[0])
sol.moveZeroes(nums=[0,1])