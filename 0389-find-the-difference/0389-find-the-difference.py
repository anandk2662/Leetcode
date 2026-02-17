class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t=list(t)
        for x in s:
            if x in t:
                t.pop(t.index(x))
        return t[0]