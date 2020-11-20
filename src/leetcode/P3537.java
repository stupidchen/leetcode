import java.util.Arrays;

/**
 * Created by mike on 3/7/18.
 */
public class Solution {
    public boolean search(int[] nums, int target) {
        int n = nums.length, i;
        if (n == 0) return false;
        for (i = 0; i < n - 1; i++)
            if (nums[i] > nums[i + 1]) break;

        return Arrays.binarySearch(nums, i + 1, n, target) >= 0 || Arrays.binarySearch(nums, 0, i + 1, target) >= 0;
    }
}
