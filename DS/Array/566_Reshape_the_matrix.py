class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if r*c != len(mat)*len(mat[0]):
            # print(mat)
            return mat
        
        else:
            reshaped_mat = [[]]

            # Step 1: make 1d array
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    next = mat[i][j]

                    if len(reshaped_mat[-1]) < c:
                        reshaped_mat[-1].append(next)
                    else:
                        reshaped_mat.append([next])
            
            # print(reshaped_mat)
            return reshaped_mat

sol = Solution()
sol.matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4)
sol.matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4)
sol.matrixReshape([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]],42,5)