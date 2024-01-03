class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        d=defaultdict(list)
        for i in access_times:
            d[i[0]].append(int(i[1]))
        res=[]
        for e in d:
            t=sorted(d[e])
            for i in range(len(t)-2):
                if t[i+2]-t[i]<100:
                    res.append(e)
                    break
        return res

        
                

