import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by mike on 4/13/16.
 */
public class P018 {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);

        List<List<Integer>> ret = new ArrayList<>();

        int n = nums.length;
        if (n <= 3) return ret;

        for (int i = 0; i < n; i++)
            if (i == 0 || nums[i] != nums[i - 1]) {
                for (int j = i + 1; j < n; j++) {
                    if (j == i + 1 || nums[j] != nums[j - 1]) {
                        for (int k = j + 1; k < n; k++) {
                            if (k == j + 1 || nums[k] != nums[k - 1]) {
                                int t = target - nums[k] - nums[i] - nums[j];
                                if (Arrays.binarySearch(nums, k + 1, n, t) >= 0) {
                                    List temp = new ArrayList<Integer>();
                                    temp.add(Integer.valueOf(nums[i]));
                                    temp.add(Integer.valueOf(nums[j]));
                                    temp.add(Integer.valueOf(nums[k]));
                                    temp.add(Integer.valueOf(t));
                                    ret.add(temp);
                                }
                            }
                        }
                    }
                }
            }

        return ret;
    }
}
