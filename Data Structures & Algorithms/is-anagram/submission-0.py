class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1=list(s)
        lst2=list(t)
        lst1.sort()
        lst2.sort()
        if lst1 == lst2:
            return True
        else:
            return False