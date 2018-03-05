import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 3/5/18.
 */
public class P077 {
    private List<List<Integer>> ret = new LinkedList<>();

    private void solve(int l, int r, int m, int n, int[] a) {
        if (m == n) {
            List<Integer> tmp = new LinkedList<>();
            for (int i = 0; i < m; i++) tmp.add(a[i]);
            ret.add(tmp);
            return;
        }

        for (int i = l; i <= r - (n - m) + 1; i++) {
            a[m] = i;
            solve(i + 1, r, m + 1, n, a);
        }
    }

    public List<List<Integer>> combine(int n, int k) {
        if (n == 0 || k == 0) return ret;

        solve(1, n, 0, k, new int[k]);

        return ret;
    }
}
