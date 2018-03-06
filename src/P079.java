/**
 * Created by mike on 3/6/18.
 */
public class P079 {
    private int[] dx = {1, -1, 0, 0};

    private int[] dy = {0, 0, 1, -1};

    private int n, m, l;

    private boolean found;

    private char[] letters;

    private boolean[][] visit;

    private char[][] board;

    private void solve(int x, int y, int t) {
        visit[x][y] = true;
        if (board[x][y] == letters[t]) {
            if (t + 1 == l) {
                found = true;
                return;
            }
            for (int i = 0; i < 4; i++) {
                int tx = x + dx[i];
                int ty = y + dy[i];
                if (tx >= 0 && ty >= 0 && tx < n && ty < m && !visit[tx][ty]) solve(tx, ty, t + 1);
                if (found) return;
            }
        }
        visit[x][y] = false;
    }

    public boolean exist(char[][] board, String word) {
        n = board.length;
        if (n == 0) return false;
        m = board[0].length;
        if (m == 0) return false;
        l = word.length();
        if (l == 0) return false;

        found = false;
        letters = word.toCharArray();
        visit = new boolean[n][m];
        this.board = board;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                solve(i, j, 0);
                if (found) return found;
            }
        return found;
    }
}
