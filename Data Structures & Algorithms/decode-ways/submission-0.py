class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0 
        prev2 = 1
        prev1 = 0

        prev1 = 1 if s[0]!='0' else 0
        for i in range(2,n+1):
            curr=0
            if s[i-1]!='0':
                curr+=prev1
            two = int(s[i-2:i])
            if 10<=two<=26:
                curr+=prev2
            
            prev2,prev1 = prev1,curr
        return prev1