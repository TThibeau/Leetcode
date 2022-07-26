class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i,j = 0,len(numbers)-1

        while i<len(numbers)-1:
            if numbers[i]+numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j] <= target:
                i += 1
            elif numbers[i]+numbers[j] >= target:
                j -= 1


sol = Solution()
sol.twoSum(numbers = [2,7,11,15], target = 9)
sol.twoSum(numbers = [2,3,4], target = 6) 
sol.twoSum(numbers = [-1,0], target = -1)
sol.twoSum([5,25,75],100)