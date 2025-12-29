class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(len(nums)-1,-1,-1):
            if len(nums)==1:
                break
            if nums[i]==nums[i-1]:
                nums.pop(i)
        return len(nums)