class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n=len(s)
        s=list(s)
        i=0
        while(i<n):
            if i+k<=n:
                s[i:i+k]=s[i:i+k][::-1]
            else:
                s[i:]=s[i:][::-1]
            i+=2*k
        return "".join(s)