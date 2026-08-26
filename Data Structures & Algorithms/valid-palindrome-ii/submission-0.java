class Solution {
    public boolean validPalindrome(String s) {
        char[] ch = s.toCharArray();
        int left = 0;
        int right = s.length()-1;
        while(left<right){
            if(ch[left]!=ch[right]){return checkPalindrome(s,left+1,right)||checkPalindrome(s,left,right-1);}
            else{left++;right--;}
        }
        return true;
    }

    private boolean checkPalindrome(String s, int left, int right){
        char[] ch = s.toCharArray();
        while(left<right){
            if(ch[left]!=ch[right])return false;
            left++;right--;
        }
        return true;
    }
}