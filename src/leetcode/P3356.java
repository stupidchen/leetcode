/**
 * Created by mike on 1/12/18.
 */

import java.util.Arrays;

public class Solution {
    public int searchInsert(int[] nums, int target) {
        int ret = Arrays.binarySearch(nums, target);
        if (ret < 0) ret = -1 - ret;
        return ret;
    }
}
