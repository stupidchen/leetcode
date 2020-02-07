/**
 * Created by mike on 2/15/18.
 */
public class P064 {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        if (m == 0) return 0;
        int n = grid[0].length;
        if (n == 0) return 0;

        int[][] f = new int[m][n];
        f[0][0] = grid[0][0];
        for (int i = 1; i < m; i++) f[i][0] = f[i - 1][0] + grid[i][0];
        for (int i = 1; i < n; i++) f[0][i] = f[0][i - 1] + grid[0][i];

        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                f[i][j] = (f[i - 1][j] > f[i][j - 1] ? f[i][j - 1] : f[i - 1][j]) + grid[i][j];

        return  f[m - 1][n - 1];
    }
}
