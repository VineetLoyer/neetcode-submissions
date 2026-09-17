class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l = 0;
        int total = 0;
        int res  = Integer.MAX_VALUE;
        for(int right = 0; right<nums.length;right++){

            total+=nums[right];
            while(total>=target){ // because we need to keep incrementing left ptr till we meet condition
                res = Math.min(right-l+1,res);
                total-=nums[l];
                l++;
            }

        }
        if(res==Integer.MAX_VALUE)return 0;
        else return res;
    }
}