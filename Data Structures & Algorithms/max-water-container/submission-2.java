class Solution {
    public int maxArea(int[] heights) {
        int maxVol=0;
        int A=0;
        int B=heights.length-1;
        while(A<B){
            int hA=heights[A];
            int hB=heights[B];
            int curVol=Math.min(hA,hB)*(B-A);
            if(curVol>maxVol)maxVol=curVol;
            if(hA>hB){
                B--;
            }
            else{A++;}
        }
        return maxVol;

    }
}
