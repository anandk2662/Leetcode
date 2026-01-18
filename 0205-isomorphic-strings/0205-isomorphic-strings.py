class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapA={}
        mapB={}
        for i in range(len(s)):
            if s[i] in mapA and t[i]!=mapA[s[i]]:
                return False
            if t[i] in mapB and s[i]!=mapB[t[i]]:
                return False
            mapA[s[i]]=t[i]
            mapB[t[i]]=s[i]
        return True