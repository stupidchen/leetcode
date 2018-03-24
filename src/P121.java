/**
 * Created by mike on 3/22/18.
 */
public class P121 {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int ret = 0, c = 0;
        for (int i = 1; i < n; i++) {
            c = Math.max(0, prices[i] - prices[i - 1] + c);
            ret = Math.max(c, ret);
        }

        return ret;
    }

    public static void main(String[] args) {
        P121 p = new P121();
        System.out.println(p.maxProfit(new int[]{7, 1, 5, 3, 6, 4}));
    }
}
