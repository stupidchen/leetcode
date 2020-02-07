/**
 * Created by mike on 2/26/18.
 */
public class P073 {
    public void setZeroes(int[][] matrix) {
        int n = matrix.length;
        if (n == 0) return;
        int m = matrix[0].length;
        if (m == 0) return;

        boolean[] r = new boolean[n];
        boolean[] c = new boolean[m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (matrix[i][j] == 0) {
                    r[i] = true;
                    c[j] = true;
                }

        for (int i = 0; i < n; i++)
            if (r[i])
                for (int j = 0; j < m; j++) matrix[i][j] = 0;

        for (int j = 0; j < m; j++)
            if (c[j])
                for (int i = 0; i < n; i++) matrix[i][j] = 0;
    }
}
