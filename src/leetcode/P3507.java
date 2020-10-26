/**
 * Created by mike on 3/11/18.
 */
public class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[][] glass = new double[110][110];
        glass[0][0] += poured;
        for (int i = 0; i < query_row + 1; i++)
            for (int j = 0; j <= i; j++) {
                if (glass[i][j] > 1) {
                    glass[i + 1][j] += (glass[i][j] - 1) / 2;
                    glass[i + 1][j + 1] += (glass[i][j] - 1) / 2;
                    glass[i][j] = 1;
                }
            }

        return glass[query_row][query_glass];
    }
}
