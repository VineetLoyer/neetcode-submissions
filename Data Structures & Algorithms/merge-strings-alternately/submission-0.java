class Solution {
    public String mergeAlternately(String word1, String word2) {
        char[] ch1 = word1.toCharArray();
        char[] ch2 = word2.toCharArray();

        int len1 = word1.length();
        int len2 = word2.length();

        char[] ch3 = new char[len1 + len2];

        int p1 = 0;
        int p2 = 0;
        int p = 0;

        while (p1 < len1 && p2 < len2) {
            ch3[p] = ch1[p1];
            ch3[p + 1] = ch2[p2];

            p += 2;
            p1++;
            p2++;
        }

        while (p1 < len1) {
            ch3[p] = ch1[p1];
            p++;
            p1++;
        }

        while (p2 < len2) {
            ch3[p] = ch2[p2];
            p++;
            p2++;
        }

        return new String(ch3);
    }
}
