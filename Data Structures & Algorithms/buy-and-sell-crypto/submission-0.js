class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let i1 = 0;
        let i2 = 1;
        let r = 0, l;
        let maxP = 0;
        
        while (i2 < prices.length){
            l = prices[i1];
            r = prices[i2];
            if (r > l){
                let profit = r - l;
                maxP = Math.max(maxP, profit);
            }else{
                i1 = i2;
            }
            i2++;
        }


        return maxP;
    }
}
