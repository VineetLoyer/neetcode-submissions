class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> hashmap_s = new HashMap<>();
        HashMap<Character,Integer> hashmap_t = new HashMap<>();
        for(char ch: s.toCharArray()){
            hashmap_s.put(ch,hashmap_s.getOrDefault(ch,0)+1);
        }
        for(char ch:t.toCharArray()){
            hashmap_t.put(ch,hashmap_t.getOrDefault(ch,0)+1);
        }

        if(hashmap_s.equals(hashmap_t)){
            return true;
        }
        return false;
    }
}
