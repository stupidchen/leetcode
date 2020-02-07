/**
 * Created by mike on 1/15/18.
 */
public class P036 {
    private int n = 9;

    private boolean validateLine(char[][] board, int line) {
        int t = (1 << n) - 1;
        for (int j = 0; j < n; j++)
            if (board[line][j] != '.') {
                if ((t | (1 << (board[line][j] - '1'))) == t) {
                    t -= 1 << (board[line][j] - '1');
                }
                else
                    return false;
            }
        return true;
    }
    private boolean validateColumn(char[][] board, int column) {
        int t = (1 << n) - 1;
        for (int i = 0; i < n; i++)
            if (board[i][column] != '.') {
                if ((t | (1 << (board[i][column] - '1'))) == t) {
                    t -= 1 << (board[i][column] - '1');
                }
                else
                    return false;
            }
        return true;
    }
    private boolean validateGrid(char[][] board, int x, int y) {
        int t = (1 << n) - 1;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (board[x + i][y + j] != '.') {
                    if ((t | (1 << (board[x + i][y + j] - '1'))) == t) {
                        t -= 1 << (board[x + i][y + j] - '1');
                    }
                    else
                        return false;
                }
        return true;
    }

    public boolean isValidSudoku(char[][] board) {
        boolean ans = true;
        for (int i = 0; i < n; i++)
            if ((!validateColumn(board, i)) || (!validateLine(board, i))) {
                ans = false;
                break;
            }
        if (ans) {
            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    if (!validateGrid(board, i * 3, j * 3)) {
                        ans = false;
                        break;
                    }
        }
        return ans;
    }
}
