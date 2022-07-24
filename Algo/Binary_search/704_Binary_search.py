class Solution:
    def search(self, nums: list[int], target: int) -> int:         
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1

# Example execution:
# [1,2,3,4],5
# pivot = 0 + (3-0) // 2 = 3//2 = 1
# left = pivot + 1 = 2
# pivot = 2 + (3-2) // 2 = 2 
# left = pivot + 1 = 3
# pivot = 3 
# left  = 4, return -1