/**
 * Created by mike on 3/27/18.
 */
public class P087 {
    private String a, b;

    private boolean[][][][] f;

    private boolean[][][][] v;

    private boolean solve(int la, int ra, int lb, int rb) {
        if (v[la][ra][lb][rb]) return f[la][ra][lb][rb];
        if (la == ra) {
            f[la][ra][lb][rb] = a.charAt(la) == b.charAt(lb);
            return f[la][ra][lb][rb];
        }

        for (int i = la; i < ra; i++) {
            f[la][ra][lb][rb] = solve(la, i, lb, lb + i - la) && solve(i + 1, ra, lb + i + 1 - la, rb);
            f[la][ra][lb][rb] = f[la][ra][lb][rb] || (solve(la, i, rb - (i - la), rb) && solve(i + 1, ra, lb, rb - (i - la + 1)));
            if (f[la][ra][lb][rb]) break;
        }
        return f[la][ra][lb][rb];
    }
    public boolean isScramble(String s1, String s2) {
        int n = s1.length();
        f = new boolean[n][n][n][n];
        v = new boolean[n][n][n][n];
        a = s1; b = s2;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                int[] c = new int[128];
                for (int k = 0; j + k < n && i + k < n; k++) {
                    c[s1.charAt(i + k)]++;
                    c[s2.charAt(j + k)]--;
                    int count = 0;
                    for (char q = 'A'; q <= 'z'; q++)
                        if (c[q] != 0) {
                            count++;
                            break;
                        }

                    if (count != 0) v[i][i + k][j][j + k] = true;
                }
            }
        return solve(0, n - 1, 0, n - 1);
    }

    public static void main(String[] args) {
        P087 p = new P087();
        System.out.println(p.isScramble("vfldiodffghyq", "vdgyhfqfdliof"));
    }
}
