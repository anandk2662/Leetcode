class Solution(object):
    def calHours(self,piles,mid):
        hours=0
        for i in range(0,len(piles)):
            hours+=(piles[i]+mid-1)//mid
        return hours
    def minEatingSpeed(self, piles, h):    
        low,high=1,max(piles)
        ans=high
        while(low<=high):
            mid=(low+high)//2
            hours=self.calHours(piles,mid)
            if hours<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
