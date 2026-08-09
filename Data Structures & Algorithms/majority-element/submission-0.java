class Solution {
    public int majorityElement(int[] nums) {
        // boyer moore Algo - candidate, vote.
        // initially candidate = -1, vote = 0;
        // traverse the array; if vote==0, set candidate = arr[i] and vote to 1.
        // if arr[i]=candidate, vote++;
        // else, vote--;

        // count occurances of candidate, if >n/2; return that else -1.

        int candidate=-1;
        int vote=0;
        for(int i=0;i<nums.length;i++){
            if(vote==0){
                candidate = nums[i];
            }
            if(nums[i]==candidate){
                vote++;
            }
            else{
                vote--;
            }
        }
        if(vote>0){
            return candidate;
        }
        return -1;
    }
}