/**
 * Created by mike on 3/15/18.
 */
public class P085 {
    public int maximalRectangle(char[][] matrix) {
        int n = matrix.length;
        if (n == 0) return 0;
        int m = matrix[0].length;
        if (m == 0) return 0;

        int[][] f = new int[n][m];
        for (int i = 0; i < n; i++) {
            f[i][0] = matrix[i][0] - '0';
            for (int j = 1; j < m; j++)
                if (matrix[i][j] == '1')
                    f[i][j] = f[i][j - 1] + 1;
                else
                    f[i][j] = 0;
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int max = f[i][j], t;
                for (int k = i - 1; k >= 0; k--) {
                    if (f[k][j] < max) max = f[k][j];
                    t = max * (i - k + 1);
                    if (t > ans) ans = t;
                }
            }
        }

        return ans;
    }
}
