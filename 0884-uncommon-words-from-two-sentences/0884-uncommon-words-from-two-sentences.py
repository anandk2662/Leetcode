class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s=s1+" "+s2
        freq={}
        for i in s.split():
            freq[i]=freq.get(i,0)+1
        ans=[]
        for key,value in freq.items():
            if value==1:
                ans.append(key)
        return ans