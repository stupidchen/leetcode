import java.lang.Math;

public class Solution {
    private int[][] f;
    private int[] dx = {1, -1, 0, 0};
    private int[] dy = {0, 0, 1, -1};

    private void updatePath(int[][] matrix, int rowSize, int colSize, int x, int y) {
        int tx, ty;
        if (f[x][y] == 0) f[x][y] = 1;
        for (int i = 0; i < 4; i++) {
            tx = x + dx[i];
            ty = y + dy[i];
            if ((tx >= 0) && (tx < rowSize) && (ty >= 0) && (ty < colSize)) {
                if (matrix[x][y] > matrix[tx][ty] && (f[tx][ty] == 0 || f[x][y] < f[tx][ty] + 1)){
                    updatePath(matrix, rowSize, colSize, tx, ty);
                    f[x][y] = Math.max(f[x][y], f[tx][ty] + 1);
                }
            }
        }
    }

    public int longestIncreasingPath(int[][] matrix) {
        int rowSize = matrix.length;
        if (rowSize == 0) return 0;
        int colSize = matrix[0].length;

        f = new int[rowSize][colSize];
        int ans = 0;
        for (int i = 0; i < rowSize; i++)
            for (int j = 0; j < colSize; j++) {
                updatePath(matrix, rowSize, colSize, i, j);
                ans = Math.max(f[i][j], ans);
            }

        return ans;
    }
}