class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1,len2 = len(s1),len(s2)
        if len1>len2:
            return False
        Counter1 = Counter(s1)
        Counter2 = Counter(s2[:len1])
        if Counter1 == Counter2:
            return True
        for i in range(len1,len2):
            Counter2[s2[i]]+=1
            Counter2[s2[i-len1]]-=1
            if Counter2[s2[i-len1]]==0:
                del Counter2[s2[i-len1]]
            if Counter1==Counter2:
                return True
        return False