class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        tarVal=ord(target)
        st,end=0,len(letters)-1
        ans=letters[0]
        while(st<=end):
            mid=(st+end)//2
            if ord(letters[mid])>tarVal:
                ans=letters[mid]
                end=mid-1
            else:
                st=mid+1
        
        return ans