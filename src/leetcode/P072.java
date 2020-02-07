/**
 * Created by mike on 3/19/18.
 */
public class P072 {
    private int min(int x, int y) {
        if (x < y) return x;
        return y;
    }

    public int minDistance(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        if (n == 0) return m;
        if (m == 0) return n;

        int[][] f = new int[n + 1][m + 1];
        for (int i = 0; i <= n; i++) f[i][0] = i;
        for (int j = 0; j <= m; j++) f[0][j] = j;

        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++) {
                f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1);
                if (word1.charAt(i - 1) == word2.charAt(j - 1))
                    f[i][j] = min(f[i][j], f[i - 1][j - 1]);
                else
                    f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1);
            }

        return f[n][m];
    }
}
