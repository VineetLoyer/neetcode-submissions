# from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Approach 1 : Using sorted() function - given merge sort is used in background 
        #TC = O(nlogn + mlogm)
        # if sorted(s)==sorted(t):
        #     return True
        # return False
        #Approach 2: Using Hash Table
        if len(s)!=len(t):
            return False
        countS,countT={},{}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        return countS==countT
        