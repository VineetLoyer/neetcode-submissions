class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,ArrayList<String>> hashmap = new HashMap<>();
        int n = strs.length;

        for(String s: strs){
            int[] freq = new int[26];
            for(char c:s.toCharArray()){
                freq[c-'a']++;
            }
            String key = Arrays.toString(freq);
            hashmap.putIfAbsent(key,new ArrayList<>());
            hashmap.get(key).add(s);
        }
        return new ArrayList<>(hashmap.values());

    }
}
