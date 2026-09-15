class Solution {
    public int lengthOfLongestSubstring(String s) {
        /*
        - if i start from beginning z, zx,zxy, zxyz, so valid is zxy of length 3, question is "when i find duplicate, do i really need to start over?" maybe not. 
        - I can have a window which represents the substring i am considering right now. [left,...,right]
        - rule is everything inside the window is unique.
        - as i see a duplicate, what i can do is make left move until the duplicate is gone.

        - what i need is two things in this sliding widow approach, left  = where my current substring starts;  and a set containing the characters currently inside the window.

        - when i see a character thats already in the set, i keep removing characters from the left until the duplicate disappears.

        - then i add the current character and calculate the winodw length.


        */

        Set<Character> characterInWindow = new HashSet<>();
        int left = 0;
        int longestLen = 0;
        for(int right = 0; right<s.length(); right++){
            char currentCharacter = s.charAt(right);
            while(characterInWindow.contains(currentCharacter))
            {
                char leftChar = s.charAt(left);
                characterInWindow.remove(leftChar);
                left++;
            }

            characterInWindow.add(currentCharacter);
            int currentLen = right-left+1;
            if(currentLen>longestLen){
                longestLen = currentLen;
            }
        }
        return longestLen;
    }
}
