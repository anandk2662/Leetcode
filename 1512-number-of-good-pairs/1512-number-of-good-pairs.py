class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        freq={}
        for x in nums:
            count+=freq.get(x,0)
            freq[x]=freq.get(x,0)+1
        return count