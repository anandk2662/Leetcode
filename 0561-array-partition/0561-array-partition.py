class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        Sum=0
        for i in range(0,len(nums),2):
            Sum+=nums[i]
        return Sum