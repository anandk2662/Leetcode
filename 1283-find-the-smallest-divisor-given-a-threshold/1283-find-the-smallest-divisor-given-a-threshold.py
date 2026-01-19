class Solution(object):
    def Possible(self,n,d):
        count=0
        for i in n:
            count+=((i+d-1)//d)
        return count
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low,high=1,max(nums)
        ans=high
        while(low<=high):
            mid=(low+high)>>1
            if self.Possible(nums,mid)<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans