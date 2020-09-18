/**
 * Created by mike on 3/22/18.
 */
public class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int ret = 0, c = 0;
        for (int i = 1; i < n; i++) {
            c = Math.max(0, prices[i] - prices[i - 1] + c);
            ret = Math.max(c, ret);
        }

        return ret;
    }
}
