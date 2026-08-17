class Solution {
    public boolean isAnagram(String s, String t) {
        int[] freqS = new int[26];
        int[] freqT = new int[26];

        int m = s.length();
        int n = t.length();

        if(m!=n)return false;

        for(int i=0;i<m;i++){
            freqS[s.charAt(i)-'a']++;
            freqT[t.charAt(i)-'a']++;
        }

        if(Arrays.equals(freqS,freqT))return true;

        return false;
    }
}
