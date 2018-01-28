/**
 * Created by mike on 1/28/18.
 */
public class P775 {
    public boolean isIdealPermutation(int[] A) {
        int n = A.length;
        int l = 0, r = 0;
        for (int i = 0; i < n - 1; i++) {
            if (r - l > n - i) return false;
            if (A[i] > A[i + 1]) l++;
            for (int j = i + 1; j < n; j++)
                if (A[i] > A[j]) r++;
        }
        return l == r;
    }
}
