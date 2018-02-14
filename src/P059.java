/**
 * Created by mike on 2/14/18.
 */
public class P059 {
    private int[] dx = {0, 1, 0, -1};

    private int[] dy = {1, 0, -1, 0};

    public int[][] generateMatrix(int n) {
        int[][] ret = new int[n][n];

        int x = 0, y = 0, d = 0, t = 0;
        while (t++ < n * n) {
            ret[x][y] = t;
            int tx = x + dx[d], ty = y + dy[d];
            if (tx >= 0 && tx < n && ty >= 0 && ty < n && ret[tx][ty] == 0) {
                x = tx;
                y = ty;
            }
            else {
                d = (d + 1) % 4;
                x += dx[d];
                y += dy[d];
            }
        }

        return ret;
    }
}
