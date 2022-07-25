class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # # Solution 1: Brute force - Time complexity O(N^2)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i]+nums[j] == target and i != j:
        #             return i,j 

       # Solution 2: Using a hash map
        map = {}

        for i in range(len(nums)):
            map[f"{i}"] = nums[i]

            required_value = target - nums[i]
            keys = [k for k, v in map.items() if v == required_value]
            if len(keys)>=1 and int(keys[0])!=i:
                return int(keys[0]),i
        
        same = [v for k,v in map.items() if v == target]
        if same:
            return same

sol = Solution()
indices = sol.twoSum(nums = [2,7,11,15], target = 9)
print(indices)
indices = sol.twoSum(nums=[3,2,4], target = 6)
print(indices)
indices = sol.twoSum(nums = [3,3], target = 6)
print(indices)
indices = sol.twoSum(nums = [0,3,2,0], target = 0)
print(indices)
