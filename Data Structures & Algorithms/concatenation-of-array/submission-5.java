class Solution {
    public int[] getConcatenation(int[] nums) {
        int len = nums.length;
        int[] ans = new int[2*len];
        for(int i=0;i<2*len;i++){
            ans[i] = nums[i%len];
        }
        return ans;
    }
}
// dry run
// ex: nums = [1,4,1,2]
// len = 4, ans= [ , , , , , , , ]
// i=0; ans[0] = nums[0%4] = nums[0] => [1, , , , , , ]
// i=1; ans[1] = nums[1] => [1,4, , , , , ]
// i=2,and i=3 => [1,4,1,2, , , , ]
// i=4, ans[4] = nums[4%4] = nums[0] => [1,4,1,2,1, , , ]
//.. so on