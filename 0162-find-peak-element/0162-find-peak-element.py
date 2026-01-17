class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st,end=1,len(nums)-2
        if len(nums)==1:
            return 0
        if(nums[0]>nums[1]):
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        
        while(st<=end):
            mid=st+(end-st)//2
            if(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                return mid
            elif nums[mid-1]>nums[mid]:
                end=mid-1
            else:
                st=mid+1
            

        