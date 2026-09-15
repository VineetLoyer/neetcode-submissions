class Solution {
    public int characterReplacement(String s, int k) {
        // for current substring, how many replacements would i need to make for everycharacter to be the same.
        // so, if one character already occurs more than every other character, i should keep that character and replace others to this character.
        // replacement needed = window length - freq of most common character

        int[] freq = new int[26];
        int left = 0;
        int longestLength = 0;
        int maxFreq = 0;
        for(int right = 0; right<s.length();right++){
            char currentChar = s.charAt(right);
            int currentIndex = currentChar - 'A';
            freq[currentIndex]++;

            maxFreq = Math.max(maxFreq,freq[currentIndex]);

            int windowLength  = right - left +1;
            int replacementNeeded = windowLength - maxFreq;

            while(replacementNeeded>k){
                char leftChar = s.charAt(left);
                int leftIndex = leftChar-'A';
                freq[leftIndex]--;
                left++;

                windowLength = right-left+1;
                replacementNeeded = windowLength - maxFreq;
            }
            int currentLen = right-left+1;
            if(currentLen>longestLength){
                longestLength = currentLen;
            }

        }
        return longestLength;
    }
}
