class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalEven=0
        totalOdd=0

        for i,num in enumerate(nums):
            if i%2==0:
                totalEven+=num
            else:
                totalOdd+=num
        
        leftEven=0
        leftOdd=0
        count=0

        for i,num in enumerate(nums):
            if i%2==0:
                rightEven=totalEven-leftEven-num
                rightOdd=totalOdd-leftOdd
            else:
                rightEven=totalEven-leftEven
                rightOdd=totalOdd-leftOdd-num
            
            newEven=leftEven+rightOdd
            newOdd=leftOdd+rightEven

            if newEven==newOdd:
                count+=1
            
            if i%2==0:
                leftEven+=num
            else:
                leftOdd+=num
        return count
