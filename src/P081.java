import java.util.Arrays;

/**
 * Created by mike on 3/7/18.
 */
public class P081 {
    public boolean search(int[] nums, int target) {
        int n = nums.length, i;
        if (n == 0) return false;
        for (i = 0; i < n - 1; i++)
            if (nums[i] > nums[i + 1]) break;

        return Arrays.binarySearch(nums, i + 1, n, target) >= 0 || Arrays.binarySearch(nums, 0, i + 1, target) >= 0;
    }

    public static void main(String[] args) {
        P081 p = new P081();
        System.out.println(p.search(new int[]{4, 0, 1, 2}, 4));
    }
}
