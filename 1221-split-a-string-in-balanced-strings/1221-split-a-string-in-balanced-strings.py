class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countL,countR=0,0
        split=0
        for i in s:
            if countR==countL:
                split+=1
                countL=0
                countR=0

            if i=="R":
                countR+=1
            else:
                countL+=1
        return split