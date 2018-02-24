/**
 * Created by mike on 2/24/18.
 */
public class P074 {
    public int getElement(int[][] matrix, int n, int m, int index) {
        if (index < 0 || index >= n * m) return -1;
        return matrix[index / m][index % m];
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        int n = matrix.length;
        if (n == 0) return false;

        int m = matrix[0].length;
        if (m == 0) return false;

        int l = 0, r = n * m - 1, mid;
        while (l <= r) {
            mid = (l + r) >> 1;
            int t = getElement(matrix, n, m, mid);
            if (t == target) return true;
            if (t < target)
                l = mid + 1;
            else
                r = mid - 1;
        }

        return false;
    }
}
