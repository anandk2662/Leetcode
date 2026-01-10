class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        st,end=0,len(nums)-1
        while(st<=end):
            mid=st+(end-st)//2
            if nums[mid]==target:
                return mid
            #left sorted
            elif nums[st]<=nums[mid]:
                if target<=nums[mid] and target>=nums[st]:
                    end=mid-1
                else:
                    st=mid+1
            else:
                if target>=nums[mid] and target<=nums[end]:
                    st=mid+1
                else:
                    end=mid-1
        return -1
            
        