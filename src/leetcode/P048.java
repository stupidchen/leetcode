/**
 * Created by mike on 1/18/18.
 */
public class P048 {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        if (n == 0) return;
        int tmp[][] = new int[n][n];

        for (int i = 0; i < n; i++)
            System.arraycopy(matrix[i], 0, tmp[i], 0, n);

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                matrix[j][n - i - 1] = tmp[i][j];
            }
    }
}
