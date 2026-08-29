class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int n = people.length;
        Arrays.sort(people);
        int A=0;
        int B=n-1;
        int boats=0;
        while(A<=B){
            if(people[A]+people[B]<=limit){
                boats++;
                A++;
                B--;

            }
            else{
                boats++;
                B--;
            }
        }
        return boats;
    }
}