import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by mike on 1/17/18.
 */
public class Solution {
    private boolean hasNext(int[] nums) {
        for (int i = 1; i < nums.length; i++)
            if (nums[i] > nums[i - 1]) return true;
        return false;
    }

    private List<Integer> generateFromArray(int[] a) {
        List<Integer> ret = new ArrayList<Integer>();
        for (int i = 0; i < a.length; i++) ret.add(a[i]);
        return ret;
    }

    private void swap(int[] a, int x, int y) {
        int t = a[x];
        a[x] = a[y];
        a[y] = t;
    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ans = new LinkedList<>();
        Arrays.sort(nums);
        ans.add(generateFromArray(nums));
        int n = nums.length;
        while (hasNext(nums)) {
            int i;
            for (i = n - 1; i > 0; i--)
                if (nums[i] > nums[i - 1]) break;
            for (int j = n - 1; j >= i; j--)
                if (nums[i - 1] < nums[j]) {
                    swap(nums, j, i - 1);
                    break;
                }
            Arrays.sort(nums, i, nums.length);
            ans.add(generateFromArray(nums));
        }
        return ans;
    }
}