class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = []
        for row in range(numRows):
            next_row = []
            for j in range(row+1):
                if j == 0 or j == row:
                    next = 1
                else:
                    next = ans[row-1][j-1]+ans[row-1][j]
                next_row.append(next)
            ans.append(next_row)
        return ans

sol = Solution()
result = sol.generate(5)
print(result)
