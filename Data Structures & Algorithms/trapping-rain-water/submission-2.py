class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height)-1
        LM,RM = height[l],height[r]
        res = 0
        while l<r:
            if LM < RM:
                l+=1
                LM = max(LM,height[l])
                res+= LM - height[l]
            else:
                r-=1
                RM = max(RM,height[r])
                res+= RM - height[r]
        return res