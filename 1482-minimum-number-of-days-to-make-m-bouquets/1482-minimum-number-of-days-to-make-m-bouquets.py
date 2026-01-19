class Solution(object):
    def Valid(self,b,d,k):
        count,NoOfBloom=0,0
        for i in b:
            if(i<=d):
                count+=1
            else:
                NoOfBloom+=(count//k)
                count=0
        NoOfBloom+=(count//k)
        return NoOfBloom
    
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if(m*k>len(bloomDay)):
            return -1
        low,high=min(bloomDay),max(bloomDay)+1
        ans=high
        while(low<=high):
            mid=(low+high)>>1
            if (self.Valid(bloomDay,mid,k)>=m):
                ans=mid
                high=mid-1
            else:
                low=mid+1
            
        return ans
