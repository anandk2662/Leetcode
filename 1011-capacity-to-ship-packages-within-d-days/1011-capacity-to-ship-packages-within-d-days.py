class Solution(object):
    def Possible(self,w,cap):
        count,days=0,1
        for i in w:
            if count+i<=cap:
                count+=i
            else:
                days+=1
                count=i
        return days
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low,high=max(weights),sum(weights)
        ans=high
        while(low<=high):
            mid=(low+high)>>1
            if self.Possible(weights,mid)<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans