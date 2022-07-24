# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
import unittest as ut
import os
os.system('cls')
# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         squared_nums = []
#         for element in nums:
#             squared_nums.append(element**2)
        
#         sorted_nums = sorted(squared_nums)
#         return sorted_nums
        
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        new_nums = []

        left,right = 0,len(nums)-1

        while left<=right:
            if nums[left]**2 > nums[right]**2:
                new_nums.append(nums[left]**2)
                left +=1
            else:
                new_nums.append(nums[right]**2)
                right -=1
        return new_nums[::-1]


sol = Solution()
ut.TestCase().assertEqual(sol.sortedSquares([-4,-1,0,3,10]),[0,1,9,16,100])
ut.TestCase().assertEqual(sol.sortedSquares([-7,-3,2,3,11]),[4,9,9,49,121])
ut.TestCase().assertEqual(sol.sortedSquares([-5,-3,-2,-1]),[1,4,9,25])