class Solution:
    def findDuplicates(self, arr):
        # code here
        seen=set()
        res=[]
        for i in arr:
            if i in seen:
                res.append(i)
            else:
                seen.add(i)
        return res
