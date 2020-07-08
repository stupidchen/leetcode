import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by mike on 4/10/16.
 */
public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> ret = new ArrayList<>();

        int n = nums.length;
        if (n <= 2) return ret;

        for (int i = 0; i < n; i++)
            if (i == 0 || nums[i] != nums[i - 1]) {
                for (int j = i + 1; j < n; j++) {
                    if (j == i + 1 || nums[j] != nums[j - 1]) {
                        int t = 0 - nums[i] - nums[j];
                        if (Arrays.binarySearch(nums, j + 1, n, t) >= 0) {
                            List temp = new ArrayList<Integer>();
                            temp.add(Integer.valueOf(nums[i]));
                            temp.add(Integer.valueOf(nums[j]));
                            temp.add(Integer.valueOf(t));
                            ret.add(temp);
                        }
                    }
                }
            }

        return ret;
    }
}
