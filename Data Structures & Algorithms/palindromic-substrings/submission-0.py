class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n<=1:
            return n
        
        def expand(l:int,r:int) -> int:
        
            cnt=0
            while l>=0 and r<n and s[l]==s[r]:
                cnt+=1
                l-=1
                r+=1
            return cnt
        total=0
        for i in range(n):
            total+=expand(i,i)
            total+=expand(i,i+1)
        return total