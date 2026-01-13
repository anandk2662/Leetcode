class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique=len(set(nums))
        if unique!=len(nums):
            return True
        else:
            return False