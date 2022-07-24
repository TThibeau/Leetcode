# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,\
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad.\
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Binary search through the list? Time complexity O(log n)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 0,n-1
        pivot = 0
        def isBadVersion(index):
            versions = [False,True,True]
            return versions[index-1]

        while left<=right:
            pivot = left + (right-left)//2
            print(f"pivot: {pivot}, left: {left}, right: {right},")
            if isBadVersion(pivot+1) == True:
                right = pivot - 1
            if isBadVersion(pivot+1) == False:
                left = pivot +1
        
        if isBadVersion(pivot+1) == True:
            return pivot+1
        if isBadVersion(pivot+2)==True:
            return pivot+2

sol = Solution()
result = sol.firstBadVersion(3)
print(result)