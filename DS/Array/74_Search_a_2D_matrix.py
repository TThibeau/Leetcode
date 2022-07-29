class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Make a list of the first column
        # binary search through this list checking: 
            # if list[i] < target and if list[i+1]> target: 
                # binary search in row i
                    # if found: return True
                    # else: return False
            # if list[i+1] < target:
                # new i UP
            # if list[i] > target:
                # new i DOWN
        
        # Make a list of the first column
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
        
# credit to neetcode.io

sol = Solution()
result = sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)
print(result)
result = sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)
print(result)
result = sol.searchMatrix([[1]],0)
print(result)
result = sol.searchMatrix([[1,3]],3)
print(result)
            