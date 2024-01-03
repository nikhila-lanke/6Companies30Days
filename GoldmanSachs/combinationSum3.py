class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def bt(num,li,target):
            if len(li)==k:
                if target==0:
                    res.append(li)
                return
            for i in range(num+1,10):
                if i<=target:
                    bt(i,li+[i],target-i)
                else:
                    return 
        bt(0,[],n)
        return res
