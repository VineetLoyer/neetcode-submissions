class Solution {
    public void rotate(int[] nums, int k) {
        
        int n = nums.length;int nk=k%n;
        reverse(nums,0,n-1);
        reverse(nums,0,nk-1);
        reverse(nums,nk,n-1);
    }
    private static int[] reverse(int[] nums, int start, int end){
        while(start<=end){
            int temp=nums[start];
            nums[start]=nums[end];
            nums[end]=temp;
            start++;
            end--;
        }return nums;
}
}