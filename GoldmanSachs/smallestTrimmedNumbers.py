class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        d={}
        res=[]
        for k,t in queries:
            if t not in d:
                d[t]=sorted([(j[-t:],i)for i,j in enumerate(nums)])
            res.append(d[t][k-1][1])
        return res
