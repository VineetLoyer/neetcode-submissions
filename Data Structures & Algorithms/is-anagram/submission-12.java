class Solution {
    public boolean isAnagram(String s, String t) {
// brute force - 
// i check if s and t are of same length - if not return false;
// i convert them to char array and sort them, check. => TC O(nlogn) SC O(n)

// optimize 
// convert the two strings into hashmap a and b; Char:Freq => {r:2,a:2} => compare the hashmaps.

// since, we are given that, s and t both have lowercase english char => freq integer array. where index 0 = 'a', 1 = 'b'... O(26) ~ O(1) SC ; O(n) tc
    int[] str1 = new int[26];
    int[] str2 = new int[26];
    if(s.length() != t.length()){
        return false;
    }
    for(int i=0;i<s.length();i++){
        str1[s.charAt(i)-'a']++; 
        str2[t.charAt(i)-'a']++;
    }

    if(Arrays.equals(str1,str2)){
        return true;
    }
    return false;

    }
}
