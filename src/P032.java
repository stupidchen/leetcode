/**
 * Created by mike on 2/5/18.
 */

public class P032 {
    public int longestValidParentheses(String s) {
        if (s == null || s.length() == 0) return 0;

        int n = s.length();
        int[] f = new int[n];

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(') {
                f[i] = -1;
                continue;
            }
            f[i] = -1;
            if (i > 0 && s.charAt(i - 1) == '(') f[i] = 2;
            if (i > 0 && f[i - 1] != -1) {
                int t = i - 1 - f[i - 1];
                if (t >= 0 && s.charAt(t) == '(') f[i] = f[i - 1] + 2;
            }

            int t = i - f[i];
            if (f[i] != -1 && t > 0 && f[t] != -1) f[i] += f[t];

            if (f[i] > ans) ans = f[i];
        }

        return ans;
    }

    public static void main(String[] args) {
        P032 p = new P032();
        System.out.println(p.longestValidParentheses("(()()()()))))(())())"));
    }
}
