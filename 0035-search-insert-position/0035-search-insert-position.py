class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        found=False
        for i in range(len(nums)):
            if nums[i]==target:
                found=True
                return i
        if not found:
            for i in range(len(nums)):
                if nums[-1]<target:
                    return len(nums)
                elif nums[i]>target:
                    return i
                        
                
            