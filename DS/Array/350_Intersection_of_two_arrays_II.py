class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Output list is of size equal to smallest list of the two
        # can use a hash table to keep track if available in bigger list
        if len(nums1)>len(nums2): 
            small = nums2
            big = nums1

        else: 
            small = nums1
            big = nums2

        available = {} # map with keys of values already seen in big list
        output = []

        for j in big:
            if f"{j}" in available.keys():
                available[f"{j}"] += 1
            else:
                available[f"{j}"] = 1
                
        for i in range(len(small)):
            if f"{small[i]}" in available.keys():
                output.append(small[i])
                available[f"{small[i]}"] -= 1
                if available[f"{small[i]}"] == 0:
                    del(available[f"{small[i]}"])

        # print(output)
        return output
            

sol = Solution()
sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2])
sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
