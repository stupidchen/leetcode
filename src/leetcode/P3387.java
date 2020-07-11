import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 3/1/18.
 */
public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        int n = nums.length;
        List<List<Integer>> ret = new LinkedList<>();

        int m = (1 << n) - 1;
        for (int i = 0; i <= m; i++) {
            List<Integer> tmp = new LinkedList<>();
            for (int j = 0; j < n; j++)
                if ((i | (1 << j)) == i) tmp.add(nums[j]);
            ret.add(tmp);
        }

        return ret;
    }
}
