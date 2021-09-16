import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 2/10/18.
 */
public class Solution {
    private int[] dx = {0, 1, 0, -1};

    private int[] dy = {1, 0, -1, 0};

    public List<Integer> spiralOrder(int[][] matrix) {
        int n = matrix.length;
        List<Integer> ret = new LinkedList<>();
        if (n == 0) return ret;
        int m = matrix[0].length;
        if (m == 0) return ret;

        int x = 0, y = 0, d = 0, t = 0;
        while (t++ < n * m) {
            ret.add(matrix[x][y]);
            matrix[x][y] = 0;
            int tx = x + dx[d], ty = y + dy[d];
            if (tx >= 0 && tx < n && ty >= 0 && ty < m && matrix[tx][ty] != 0) {
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
