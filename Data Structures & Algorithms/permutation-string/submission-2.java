class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int l1 = s1.length();
        int l2 = s2.length();

        if (l1 > l2) return false;

        int[] s1Count = new int[26];
        int[] s2Count = new int[26];

        // Initialize the first window
        for (int i = 0; i < l1; i++) {
            s1Count[s1.charAt(i) - 'a']++;
            s2Count[s2.charAt(i) - 'a']++;
        }

        int matches = 0;
        for (int i = 0; i < 26; i++) {
            if (s1Count[i] == s2Count[i]) {
                matches++;
            }
        }

        int left = 0;
        // Slide the window
        for (int right = l1; right < l2; right++) {
            if (matches == 26) return true;
            
            // 1. Process the new character entering the window on the right
            int index = s2.charAt(right) - 'a';
            s2Count[index]++;
            if (s1Count[index] == s2Count[index]) {
                matches++;
            } else if (s1Count[index] + 1 == s2Count[index]) {
                matches--;
            }

            // 2. Process the old character leaving the window on the left
            int index1 = s2.charAt(left) - 'a';
            s2Count[index1]--;
            if (s1Count[index1] == s2Count[index1]) {
                matches++;
            } else if (s1Count[index1] - 1 == s2Count[index1]) {
                matches--;
            }

            left++;
        }
        
        // Check the final window
        return (matches == 26);
    }
}