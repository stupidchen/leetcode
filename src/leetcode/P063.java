/**
 * Created by mike on 2/19/18.
 */
public class P063 {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        if (m == 0) return 0;
        int n = obstacleGrid[0].length;
        if (n == 0 || obstacleGrid[0][0] == 1) return 0;

        int[][] f = new int[m][n];
        f[0][0] = 1;
        for (int i = 1; i < m; i++) {
            if (obstacleGrid[i][0] == 1) break;
            f[i][0] = 1;
        }
        for (int j = 1; j < n; j++) {
            if (obstacleGrid[0][j] == 1) break;
            f[0][j] = 1;
        }

        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                if (obstacleGrid[i][j] != 1) f[i][j] = f[i - 1][j] + f[i][j - 1];

        return f[m - 1][n - 1];
    }
}
