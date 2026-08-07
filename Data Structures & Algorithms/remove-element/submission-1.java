class Solution {
    public int removeElement(int[] nums, int val) {
        int slow = 0;
        int fast = 0;
        int n = nums.length;
        while(fast < n){
            if (nums[fast] != val) {
                if(slow!=fast){nums[slow] = nums[fast];}
                slow++;
            }
            fast++;
        }
        return slow;
    }
}

// [3,2,2,3] val=3
// slow=0,fast=0
// fast<4 
// nums[fast]=3, skip;fast=1
// nums[fast]=2, = val -> swap. [2,3,2,3] slow=1, fast=2
// nums[fast]=2, val -> swap. [2,2,3,3] slow=2, fast=3
// fast<n -> exit return slow, 2
