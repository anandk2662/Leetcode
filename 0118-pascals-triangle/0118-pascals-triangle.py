class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []

        for row in range(numRows):
            ansRow = [1]
            value = 1

            for i in range(1, row):
                value = value * (row - i + 1) // i
                ansRow.append(value)

            if row > 0:
                ansRow.append(1)

            ans.append(ansRow)

        return ans
        
        
        