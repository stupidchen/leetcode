import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 2/21/18.
 */
public class P051 {
    private List<List<String>> solutions;

    private int[] solution;

    private List<String> generateSolution(int n, int[] solution) {
        char[][] chessboard = new char[n][n];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) chessboard[i][j] = '.';
        for (int i = 0; i < n; i++) chessboard[i][solution[i]] = 'Q';

        List<String> ret = new LinkedList<>();
        for (int i = 0; i < n; i++) ret.add(String.valueOf(chessboard[i]));

        return ret;
    }

    private void solve(int n, int row, boolean[] column, boolean[] diagonal, boolean[] backDiagonal) {
        if (row >= n) {
            solutions.add(generateSolution(n, solution));
            return;
        }

        for (int i = 0; i < n; i++)
            if (!column[i] && !diagonal[row + i] && !backDiagonal[n + row - i]) {
                column[i] = true;
                diagonal[row + i] = true;
                backDiagonal[n + row - i] = true;
                solution[row] = i;
                solve(n, row + 1, column, diagonal, backDiagonal);
                column[i] = false;
                diagonal[row + i] = false;
                backDiagonal[n + row - i] = false;
            }
    }

    public List<List<String>> solveNQueens(int n) {
        solutions = new LinkedList<>();

        if (n == 0) return solutions;


        solution = new int[n];
        solve(n, 0, new boolean[n], new boolean[n << 1], new boolean[n << 1]);

        return solutions;
    }

    public static void main(String[] args) {
        P051 p = new P051();
        p.solveNQueens(4);
    }
}
