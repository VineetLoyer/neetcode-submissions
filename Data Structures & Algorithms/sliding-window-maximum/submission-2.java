class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        // Handle edge case for empty arrays
        if (nums == null || nums.length == 0) return new int[0];
        
        int n = nums.length;
        int[] output = new int[n - k + 1];
        int outIdx = 0;
        
        // Instantiate the Deque with a concrete class
        Deque<Integer> q = new ArrayDeque<>();

        int l = 0, r = 0;
        while (r < n) {
            // Remove elements from the back that are smaller than the current element
            while (!q.isEmpty() && nums[q.peekLast()] < nums[r]) {
                q.pollLast();
            }
            // Add current index to the back
            q.offerLast(r);

            // Remove the leftmost index if it falls out of the current window boundaries
            if (l > q.peekFirst()) {
                q.pollFirst();
            }
            
            // Once the window reaches size k, append to output and slide left pointer
            if (r + 1 >= k) {
                output[outIdx++] = nums[q.peekFirst()];
                l += 1;
            }
            r += 1;
        }
        
        return output;
    }
}
