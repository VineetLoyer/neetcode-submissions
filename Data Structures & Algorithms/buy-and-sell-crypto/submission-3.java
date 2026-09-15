class Solution {
    public int maxProfit(int[] prices) {
/*
- i need the largest profit, and if every future price is worse than the buying price, i should return 0.

- say, i am on day 2 -> when price[2] = 5
- on this day, i need to know what was the previous min price that i have seen so far. 
- profit if i sell today = current price - cheapest price of stock we saw.

- minPrice = first price
- maxProfit = 0
- for every price:
    - calculate profit if we sell today
    - if this profit is better:
        - update maxProfit
    - if today's price is cheaper
        - update minPrice
- return maxProfit
*/

    int minPrice = prices[0]; // 10
    int maxProfit = 0; // 0
    for(int i=1;i<prices.length;i++){ //i=1,i=2,i=3,i=4,i=5
        int curProfit = prices[i] - minPrice; // 0
        if(curProfit>maxProfit){ // no
            maxProfit = curProfit; // maxProfit = 6
        }
        if(prices[i]<minPrice){ // minprice = 1
            minPrice = prices[i];
        }
    }
    return maxProfit; // 6

    }
}
