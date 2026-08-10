class MyHashSet {
    // hashset cannot contain duplicate
    // max size is 10000 insertions
    // how to handle collisions? - using chaining, via LinkedList

    // array: index, LinkedList: value

    // bf: using dynamic Array
    private List<Integer> data;

    public MyHashSet() {
        data = new ArrayList<>();    
    }
    
    public void add(int key) {
        if(!data.contains(key)){
            data.add(key);
        }
        
    }
    
    public void remove(int key) {
        data.remove(Integer.valueOf(key));
    }
    
    public boolean contains(int key) {
        return data.contains(key);
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */