class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        posOf0=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]==0]
        for i in posOf0:
            r,c=i
            for i in range(len(matrix[0])):
                matrix[r][i]=0
            for j in range(len(matrix)):
                matrix[j][c]=0
                