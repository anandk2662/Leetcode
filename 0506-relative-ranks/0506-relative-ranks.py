class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        newScore=[0]*len(score)
        for i in range(1,len(score)+1):
            newScore[i-1]=(i,score[i-1])
        newScore=sorted(newScore,key=lambda x:x[1],reverse=True)
        ans=[0]*len(score)
        for pos,scor in enumerate(newScore):
            if pos==0:
                ans[scor[0]-1]="Gold Medal"
            elif pos==1:
                ans[scor[0]-1]="Silver Medal"
            elif pos==2:
                ans[scor[0]-1]="Bronze Medal"
            else:
                ans[scor[0]-1]=str(pos+1)
        return ans