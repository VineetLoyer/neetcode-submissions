class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        if n<=1:
            return s
        start,best_len = 0,1
        def expand(l:int,r:int)->None:
            nonlocal start,best_len
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            cur_len = r-(l+1)
            if cur_len > best_len:
                best_len = cur_len
                start = l+1
        for i in range(n):
            expand(i,i)
            expand(i,i+1)
        
        return s[start:start+best_len]