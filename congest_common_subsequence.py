class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # add +1 for an empty string
        matrix = [[0 for l in range(len(text1)+1)] for l in range(len(text2)+1)]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if text1[j-1] == text2[i-1]:
                    matrix[i][j] = matrix[i-1][j-1] +1
                else:
                    # see which among the two strings a character needs to be removed
                    # which will give us better output, so we take max
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
         
        # return last element of the DP (last row, last column)
        return matrix[-1][-1]
        
