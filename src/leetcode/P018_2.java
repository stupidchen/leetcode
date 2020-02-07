import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by mike on 4/13/16.
 */
public class P018_2 {
    public List<List<Integer>> fourSum(int[] nums, int target) {

        List<List<Integer>> ret = new ArrayList<>();

        int n = nums.length;
        if (n <= 3) return ret;

        Arrays.sort(nums);

        for (int i = 0; i < n; i++) {
            if ((i == 0 || nums[i] != nums[i - 1])) {
                for (int j = i + 1; j < n; j++) {
                    if (j == i + 1 || nums[j] != nums[j - 1]) {
                        int l = j + 1, r = n - 1;
                        int tempSum = target - (nums[i] + nums[j]);
                        while (l < r) {
                            if (nums[l] + nums[r] == tempSum) {
                                ret.add(Arrays.asList(nums[i], nums[j], nums[l], nums[r]));
                                while ((l < r) && (nums[l] == nums[l + 1])) l++;
                                while ((l < r) && (nums[r] == nums[r - 1])) r--;
                                l++;
                                r--;
                            }
                            else {
                                if (nums[l] + nums[r] > tempSum)
                                    r--;
                                else
                                    l++;
                            }
                        }
                    }
                }
            }
        }

        return ret;
    }
}
