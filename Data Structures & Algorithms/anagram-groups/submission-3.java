class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> hashmap = new HashMap<>();
        for(String s:strs){
            int[] count = new int[26];
            for(char c:s.toCharArray()){
                count[c-'a']++;
            }
            String key = Arrays.toString(count);
            hashmap.putIfAbsent(key, new ArrayList<>());
            hashmap.get(key).add(s);
        }
        return new ArrayList<>(hashmap.values());
    }
}
