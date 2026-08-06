class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # initial check - if length not same no need to proceed further
       if len(s) != len(t):
        return False 
       
       cc = [0]*26

       for i in range(len(s)):
        cc[ord(s[i]) - ord('a')] +=1
        cc[ord(t[i]) - ord('a')] -=1
       
       for val in cc:
        if val!=0:
            return False
       return True
        