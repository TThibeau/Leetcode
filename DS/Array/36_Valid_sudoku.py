class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # board[row][col]

        lst_row_seen = []
        lst_col_seen = []
        lst_box_seen = []
        
        for row in range(len(board)):
            lst_row_seen.append({})

            for col in range(len(board[0])):
                value = board[row][col]
                
                if value in lst_row_seen[row].keys():
                    print(f"value: {value} in row: {row}")
                    return False
                elif value != ".":
                    lst_row_seen[row][value] = None

                if row == 0:
                    lst_col_seen.append({}) # Make a dict for each col (list index indicates col index)

                if value in lst_col_seen[col].keys():
                    print(f"value: {value} in col: {col}")
                    return False
                elif value != ".":
                    lst_col_seen[col][value] = None

                if col in [0,3,6]:
                    if row in [0,3,6]:
                        lst_box_seen.append({})
                
                if row < 3: 
                    poss = [0,1,2]
                elif 3 <= row < 6:
                    poss = [3,4,5]
                elif 6 <= row:
                    poss = [6,7,8]
                
                if col < 3:
                    box = poss[0]
                elif 3 <= col < 6:
                    box = poss[1]
                elif 6 <= col:
                    box = poss[2]

                
                if value in lst_box_seen[box].keys():
                    print(f"value: {value} in box: {box}")
                    return False
                elif value != ".":
                    lst_box_seen[box][value] = None
                    
        return True

sol = Solution()
result = sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
print(result)

result = sol.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
print(result)