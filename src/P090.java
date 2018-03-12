import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 3/12/18.
 */
public class P090 {
    private List<Integer> generateSolution(int n, ArrayList<Integer> a, int[] s) {
        List<Integer> ret = new LinkedList<>();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < s[i]; j++) ret.add(a.get(i));
        return ret;
    }

    private void solve(int n, int c, ArrayList<Integer> a, ArrayList<Integer> b, int[] solution, List solutions) {
        if (c >= n) {
            solutions.add(generateSolution(n, a, solution));
            return;
        }

        for (int i = 0; i <= b.get(c); i++) {
            solution[c] = i;
            solve(n, c + 1, a, b, solution, solutions);
        }
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length, m = 0;
        ArrayList<Integer> a = new ArrayList<>();
        ArrayList<Integer> b = new ArrayList<>();
        for (int i = 0; i < n; i++)
            if (i == 0 || nums[i] != nums[i - 1]) {
                m++;
                a.add(nums[i]);
                b.add(1);
            }
            else {
                b.set(m - 1, b.get(m - 1) + 1);
            }

        List<List<Integer>> ret = new LinkedList<>();
        solve(m, 0, a, b, new int[m], ret);
        return ret;
    }

    public static void main(String[] args) {
        P090 p = new P090();
        p.subsetsWithDup(new int[]{1,2,2});
    }
}
