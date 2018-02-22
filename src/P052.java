/**
 * Created by mike on 2/21/18.
 */
public class P052 {
    private int solutions;

    private void solve(int n, int row, boolean[] column, boolean[] diagonal, boolean[] backDiagonal) {
        if (row >= n) {
            solutions++;
            return;
        }

        for (int i = 0; i < n; i++)
            if (!column[i] && !diagonal[row + i] && !backDiagonal[n + row - i]) {
                column[i] = true;
                diagonal[row + i] = true;
                backDiagonal[n + row - i] = true;
                solve(n, row + 1, column, diagonal, backDiagonal);
                column[i] = false;
                diagonal[row + i] = false;
                backDiagonal[n + row - i] = false;
            }
    }

    public int totalNQueens(int n) {
        solutions = 0;

        if (n != 0) solve(n, 0, new boolean[n], new boolean[n << 1], new boolean[n << 1]);

        return solutions;
    }
}
