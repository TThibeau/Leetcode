class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k>=len(nums):
            k = k-len(nums)
        
        back = len(nums)-k
        front = len(nums)-k-1

        temp = nums[back:] 
        nums[front:] = nums[:back]
        nums[:front] = temp
        # print(nums)

sol = Solution()
sol.rotate(nums = [1,2,3,4,5,6,7], k = 3)
sol.rotate(nums = [-1,-100,3,99], k = 2) 
sol.rotate(nums = [1,2], k = 2) 