class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=[str(i) for i in digits]
        num="".join(digits)
        num=int(num)+1
        return list(map(int,str(num)))