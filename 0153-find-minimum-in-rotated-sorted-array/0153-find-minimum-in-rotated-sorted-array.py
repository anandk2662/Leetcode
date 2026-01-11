class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st, end = 0, len(nums) - 1
        while st < end:
            mid = st + (end - st) // 2

            if nums[mid] > nums[end]:
                st = mid + 1
            else:
                end = mid

        return nums[st]