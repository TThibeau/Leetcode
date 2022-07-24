# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
 
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
import unittest as ut

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left,right = 0,len(nums)-1

        while left<=right:
            pivot = left + (right-left)//2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] < target:
                left = pivot + 1
            if nums[pivot] > target:
                right = pivot - 1

        return left

sol = Solution()
numbers = [1,3,5,6]
ut.TestCase().assertEqual(sol.searchInsert(nums=numbers,target=5),2)
ut.TestCase().assertEqual(sol.searchInsert(nums=numbers,target=2),1)
ut.TestCase().assertEqual(sol.searchInsert(nums=numbers,target=7),4)

