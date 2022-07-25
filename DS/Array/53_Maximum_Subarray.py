class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum = nums[0]
        high = nums[0]

        for i in range(1,len(nums)):
            h_t = sum + nums[i]
            t = nums[i]
            if h_t > t: sum = h_t
            else: sum = t
            if sum>high: high=sum
                
        return high

sol = Solution()
result = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(result)
result = sol.maxSubArray([1])
print(result)
result = sol.maxSubArray([5,4,-1,7,8])
print(result)