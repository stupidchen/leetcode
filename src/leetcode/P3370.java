/**
 * Created by mike on 3/17/18.
 */
public class Solution {
    public int numTrees(int n) {
        long ret = 1;
        for (int i = n + 1; i <= n << 1; i++) {
            ret = ret * i / (i - n);
        }

        return (int)(ret / (n + 1));
    }
}
