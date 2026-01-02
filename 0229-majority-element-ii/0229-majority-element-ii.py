class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        freq={}
        freqgreater3=[]
        for i in range(n):
            freq[nums[i]]=freq.get(nums[i],0)+1
        for key,value in freq.items():
            if value>n//3:
                freqgreater3.append(key)
        return freqgreater3