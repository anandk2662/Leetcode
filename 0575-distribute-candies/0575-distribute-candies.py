class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        unique=set(candyType)
        return min(len(unique),len(candyType)/2)