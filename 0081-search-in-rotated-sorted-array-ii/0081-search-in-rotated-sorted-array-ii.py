class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        st,end=0,len(nums)-1
        while st<=end:
            mid=(st+end)//2
            if nums[mid]==target:
                return True
            if nums[st]==nums[mid] and nums[mid]==nums[end]:
                st+=1
                end-=1
                continue
            elif nums[st]<=nums[mid]: #left sorted
                if target>=nums[st] and target<=nums[mid]:
                    end=mid-1
                else:
                    st=mid+1
            else:
                if target>=nums[mid] and target<=nums[end]:
                    st=mid+1
                else:
                    end=mid-1
        return False
