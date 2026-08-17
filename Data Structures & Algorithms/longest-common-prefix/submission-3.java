class Solution {
    public String longestCommonPrefix(String[] strs) {
        // horizontal scanning - 

        // take first string as prefix, compare rest of the strings one by one, character by character. I keep on truncating my prefix as per requirement. 

        String prefix = strs[0];
        for(int i=1;i<strs.length;i++){
            int j=0;
            while(j<Math.min(prefix.length(),strs[i].length())){
                if(prefix.charAt(j)!=strs[i].charAt(j)){
                    break;
                }
                j++;
            }
            prefix = prefix.substring(0,j);
        }
        return prefix;
    }
}