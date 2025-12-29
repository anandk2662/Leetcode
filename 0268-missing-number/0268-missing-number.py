class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Sum=0
        for i in range(len(nums)+1):
            Sum+=i
        return Sum-sum(nums)