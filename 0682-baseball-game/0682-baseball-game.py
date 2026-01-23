class Solution(object):
    def calPoints(self, ops):
        """
        :type operations: List[str]
        :rtype: int
        """
        arr=[]
        for i in range(len(ops)):
            try:
                arr.append(int(ops[i]))
            except ValueError:
                if ops[i]=="C":
                    arr.pop(-1)
                elif ops[i]=="D":
                    arr.append(arr[-1]*2)
                elif ops[i]=="+":
                    arr.append(arr[-1]+arr[-2])
        return sum(arr)
