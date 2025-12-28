class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest=min(strs,key=len)
        common=""
        for i in range(0,len(shortest)):
            for s in strs:
                if s[i]!=shortest[i]:
                    return common
            common+=shortest[i]
        return common