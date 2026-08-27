class Solution {
    public int removeDuplicates(int[] nums) {
        int l = 1;
        for(int r=l;r<nums.length;r++)   {
            if(nums[r]!=nums[r-1]){
                nums[l++]=nums[r];
            }
        }
        return l;
    }
}