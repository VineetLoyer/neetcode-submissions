class Solution {
    public boolean hasDuplicate(int[] nums) {
        // brute force - check each element one by one, nested loop; [1,2,3,3]; i=0; pick1 j=1 to 3; i=1; check if 2 is present from j=2 to 3; check if 3 is present ... => O(n^2), O(1)
        //  Hashset= O(1) lookup, i iterate over nums, push numbers into hashset if i have not seen them in hashset, if seen i return true.

        HashSet<Integer> hashset = new HashSet<>();
        int len = nums.length;
        for(int i=0;i<len;i++){
            if(hashset.contains(nums[i])){
                return true;
            }
            hashset.add(nums[i]);
        }
        return false;
    }
}