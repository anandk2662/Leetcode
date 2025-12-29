class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,-1,-1):
            if len(nums)==1:
                return nums
            elif nums[i]==0:
                nums.append(nums.pop(i))
        return nums