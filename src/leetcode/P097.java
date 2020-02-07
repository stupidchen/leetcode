/**
 * Created by mike on 3/27/18.
 */
public class P097 {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1 == null || s1.length() == 0) return s3.equals(s2);
        if (s2 == null || s2.length() == 0) return s3.equals(s1);
        if (s3.length() == 0) return false;
        int n = s3.length();
        int m1 = s1.length();
        int m2 = s2.length();
        if (m1 + m2 != n) return false;

        char[] b1 = s1.toCharArray();
        char[] b2 = s2.toCharArray();
        char[] a = s3.toCharArray();
        boolean[][] f = new boolean[2][m2 + 1];
        f[0][0] = true;
        for (int i = 1; i <= n; i++) {
            int c = i & 1;
            if (i > m1)
                f[c][0] = false;
            else
                f[c][0] = f[1 - c][0] && b1[i - 1] == a[i - 1];
            for (int j = 1; j <= Math.min(i, m2); j++) {
                f[c][j] = f[1 - c][j - 1] && (b2[j - 1] == a[i - 1]);
                if (i - j <= m1) {
                    boolean t = true;
                    if (i - j > 0) t = b1[i - j - 1] == a[i - 1];
                    f[c][j] = f[c][j] || (f[1 - c][j] && t);
                }
            }
        }

        return f[n & 1][m2];
    }

    public static void main(String[] args) {
        P097 p = new P097();
        System.out.println(p.isInterleave("aabcc", "dbbca", "aadbbcbcac"));
    }
}
