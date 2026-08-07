class Solution {
    /*
    given:
    - integer array nums of length n
    - 0-indexed

    todo:
    - create array ans of length 2n; ans[i]==nums[i] and ans[i+n]==nums[i]

    */
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[2*n];
        for(int i=0;i<n*2;i++){
            ans[i] = nums[i%n];
        }
        return ans;
    }
}

// n = 4
// nums[0] = 1
// [1, , , ,1, , , ]

// nums[1] = 4
// [1,4, , ,1,4, , ]

// .. so on