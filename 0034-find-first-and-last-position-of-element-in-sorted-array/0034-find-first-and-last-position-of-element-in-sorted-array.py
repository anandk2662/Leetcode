class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        st,end=0,len(nums)-1
        ans=[0,0]
        while(st<=end):
            mid=st+(end-st)//2
            if nums[mid]>=target:
                end=mid-1
            else:
                st=mid+1
        if st == len(nums) or nums[st] != target:
            return [-1, -1]
        ans[0]=st
        st,end=0,len(nums)-1
        while(st<=end):
            mid=st+(end-st)//2
            if nums[mid]>target:
                end=mid-1
            else:
                st=mid+1
        ans[1]=end
        return ans