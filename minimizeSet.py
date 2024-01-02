class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l=0; r=2**32;
        def isPossible(m: int):
            a=m-(m//divisor1)
            b=m-(m//divisor2)
            c=m-(m//(math.lcm(divisor1, divisor2)))
            return a>=uniqueCnt1 and b>=uniqueCnt2 and c>=(uniqueCnt1+ uniqueCnt2)
        while l<r:
            m=(l+r)//2
            if isPossible(m):
                r=m
            else:
                l=m+1
        return l
           
