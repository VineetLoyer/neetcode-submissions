from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # lst1=list(s)
        # lst2=list(t)
        # lst1.sort()
        # lst2.sort()
        # if lst1 == lst2:
        #     return True
        # else:
        #     return False
        # if (len(s)!=len(t)):
        #     return False
        # solution 2
        # countS,countT={},{}

        # for i in range(len(s)):
        #     countS[s[i]]=1+countS.get(s[i],0)
        #     countT[t[i]]=1+countT.get(t[i],0)
        # return countS==countT
        return Counter(s)==Counter(t)