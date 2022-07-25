class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen_dict = {}
        for element in nums:
            if f"{element}" in seen_dict.keys():
                return True                    
            else:
                seen_dict[f"{element}"] = 1
        return False

# sol = Solution()
# result = sol.containsDuplicate([1,2,3,2])
# print(result)