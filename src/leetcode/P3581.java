/**
 * Created by mike on 3/13/18.
 */
public class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        if (n == 0) return 0;

        int[] f = new int[n];
        char[] sc = s.toCharArray();
        for (int i = 0; i < n; i++) {
            int t1 = 0;
            if (sc[i] - '0' > 0) {
                if (i > 0)
                    t1 = f[i - 1];
                else
                    t1 = 1;
            }

            int t2 = 0;
            if (i > 0 && sc[i - 1] - '0' != 0) {
                int tmp = (sc[i - 1] - '0') * 10 + (sc[i] - '0');
                if (tmp > 0 && tmp <= 26) {
                    if (i > 1)
                        t2 = f[i - 2];
                    else
                        t2 = 1;
                }
            }

            if (t1 == 0 && t2 == 0) return 0;
            f[i] = t1 + t2;
        }

        return f[n - 1];
    }
}
