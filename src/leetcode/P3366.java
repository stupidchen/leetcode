/**
 * Created by mike on 2/27/18.
 */
public class Solution {
    public String getPermutation(int n, int k) {
        int[] tmp = new int[n];
        int[] cur = new int[n];
        tmp[0] = 1;
        for (int i = 1; i < n; i++) {
            tmp[i] = tmp[i - 1] * i;
            cur[i - 1] = i;
        }
        cur[n - 1] = n;

        k--;
        String ret = "";
        int m = n - 1;
        for (int i = n - 1; i >= 0; i--) {
            int t = k / tmp[i];
            k %= tmp[i];
            ret += String.valueOf(cur[t]);
            for (int j = t; j < m; j++) cur[j] = cur[j + 1];
            m--;
        }

        return ret;
    }
}
